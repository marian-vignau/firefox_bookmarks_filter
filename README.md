### **README: Firefox Bookmark Filter**

#### **Overview**
This Python script filters bookmarks exported from Firefox and creates a new HTML file containing only the bookmarks under a specific parent node. It's a handy way to extract a specific folder or category from your bookmarks without manually editing the file. This is very useful for sharing partially your bookmarks.

---

### **Features**
- **Quick Filtering** – Extracts bookmarks based on a keyword or folder name.
- **HTML Export** – Generates a clean, filtered HTML file.
- **No Overwrites** – Protects existing files by preventing overwriting unless specified.

---

### **Requirements**
- Python 3.x
- Basic understanding of how to export Firefox bookmarks to HTML.

---

### **How to Use**

1. **Export Bookmarks from Firefox**
   - In Firefox, go to `Menu > Bookmarks > Manage Bookmarks > Import and Backup > Export..." and save it as JSON file.

2. **Run the Script**
   ```bash
   python3 filter_firefox_bookmarks.py bookmarks.json "Python" -o python_bookmarks.html
   ```
   - Replace `bookmarks.html` with the path to your exported bookmarks.
   - Replace `"Python"` with the keyword or parent folder you want to filter.
   - Use `-o` to specify the output file (optional).

3. **Output**
   - The script will create an HTML file with only the bookmarks under the specified folder or matching the keyword.

---

### **Example**
**Extract bookmarks from a folder named "Projects":**
```bash
python filter_firefox_bookmarks.py bookmarks.html "Projects"
```
**Output:**
`Projects_bookmarks.html` will contain all bookmarks under "Projects."

---

### **Error Handling**
- **FileNotFoundError** – Raised if input file don't exist.
- **FileExistsError** – Raised if the output file already exists.
- **ValueError** – Raised if no bookmarks are found matching the keyword.

---

### **Why Use This Script?**
- **Organize Easily** – Extract and save only the bookmarks you need.
- **Share bookmarks** – Share an entire category of bookmarks without having to share all.
- **Backup Important Sections** – Create separate backup files for different categories.
- **Save Time** – Avoid manually editing large bookmark files.

---

### **Contributing**
Feel free to suggest improvements or contribute to the project by submitting pull requests.

---

### **License**
This project is licensed under the MIT License.
