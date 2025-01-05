import argparse
import json

from pathlib import Path

class FilterFirefox:
    def __init__(self, args):
        """Init and validate needed parameters."""
        
        self.status = ""
        self.keyword = args.keyword
        self.input = Path(args.file)
        if not self.input.exists():
            raise FileNotFoundError(f"Bookmarks '{args.file}' file must exists")
        output_file = args.output
        if not output_file:
            output_file = f"{args.keyword}_bookmarks.html"
        self.output = Path(output_file)
        if self.output.exists():
            raise FileExistsError(f"The file '{output_file}' already exists. Choose a different output name or delete the existing file.")

    def run(self):
        """Process the file and writes the output."""
        with self.input.open() as fh:
            data = json.load(fh)
        root_node = self.search(data)
        if not root_node:
            raise ValueError(f"Item '{self.keyword}' not found in the file.")
        out_data = self.generate_tree(root_node, self.format_item_html)
                
        with self.output.open("w") as fh:
            fh.write('\n'.join(out_data))
        self.status = f"File '{str(self.output)}' created with {len(out_data)} lines."
        
    def search(self, node):
        """Recursively search into the json file."""
        if "title" in node and node["title"] == self.keyword:
            return node
        if "children" in node:
            for child in node["children"]:
                found = self.search(child)
                if found is not None:
                    return found
        return None
        

    @staticmethod
    def format_item_html(item, level):
        """Format an item or title to be added to html output."""
        if len(item.get("children",[])) > 0:
            lvl = min(level, 6)  # max header level in html is H6
            return f'<h{lvl}>{item.get("title","")}</h{lvl}>'
        if item.get("title",""):
            return f'<li><a href="{item.get("uri", "")}">{item.get("title","")}</a></li>'
        return "<hr>"   

    def generate_tree(self, root, format_fn, level=1):
        """Recursively search the root node and add all descendants."""
        
        out = [format_fn(root, level)]
        if root.get("children",[]):
            out.append("<ul>")
            for child in root.get("children",[]):
                out.extend(self.generate_tree(child, format_fn, level+1))
            out.append("</ul>")
        return out
                   
def parse_arguments():
    """Take the command line arguments and give some help."""

    parser = argparse.ArgumentParser(description="Filter Firefox bookmarks by keyword and export to HTML.")
    parser.add_argument("file", help="Path to the exported Firefox bookmarks HTML file to process.")
    parser.add_argument("keyword", help="Keyword to search for in the bookmarks.")
    parser.add_argument("-o", "--output", help="Optional output file name for the filtered bookmarks.", default=None)
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    try:
        worker = FilterFirefox(args)
        worker.run()
        print(worker.status)
    except Exception as e:
        print(e)
    




