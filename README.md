Вот профессионально оформленный `README.md` для вашей программы:

---

# PDF to AutoCAD LISP Importer

A Python script that automates the generation of AutoLISP code to batch-import multiple PDF files into AutoCAD as referenced blocks, positioned sequentially on the drawing space.

## 📌 Overview

This tool scans a directory structure (`pdf/`) containing PDF files, extracts their page dimensions, and generates `.lsp` files (one per PDF) with AutoLISP commands to import each PDF page as a block at precise coordinates. It supports multi-page PDFs and can optionally arrange pages into "leaves" (rows) based on a specified page count per row.

Generated LISP code is compatible with AutoCAD’s `._import` command and uses a scale factor of `25.4` (mm to drawing units) and zero rotation.

## ✨ Features

- Automatically detects PDF page sizes (in mm) using `/MediaBox`.
- Generates individual `.lsp` files per PDF for modular use.
- Optionally generates a master `all.lsp` file combining all imports.
- Supports hierarchical layout: pages are placed horizontally until a "leaf" (row) is full, then moves to the next row.
- Reports pages with missing `/MediaBox` data for debugging.
- Uses UTF-8 input and CP1251 encoding for LISP output (compatible with Russian AutoCAD installations).

## 🛠️ Requirements

- Python 3.7+
- `pypdf` library:  
  ```bash
  pip install pypdf
  ```

## 📂 Directory Structure

```
project/
├── pdf/                     ← Place your PDF files here
│   ├── document1.pdf
│   ├── document2.pdf
│   └── subfolder/document3.pdf
├── insert_pdf.py            ← This script
├── all.lsp                  ← Combined LISP (optional)
└── document1.lsp            ← Generated per-PDF LISP files
```

> 💡 **Note**: All PDFs must be located under the `pdf/` folder. Subdirectories are supported.

## 🚀 Usage

1. Place your PDF files into the `pdf/` directory (including nested folders).
2. Run the script:
   ```bash
   python insert_pdf.py
   ```
3. In AutoCAD:
   - Type `InsertPdf` and press Enter to load and execute the generated LISP.
   - Use `all.lsp` for bulk import or individual `.lsp` files for targeted imports.

## 🔧 Customization

- **Page layout**: Modify `count_pages_in_leaf` in `insert_pdf()` to define how many pages per row (e.g., `[3, 2]` → first row: 3 pages, second: 2 pages).
- **Scale**: Adjust the `scale` value in `PageSize` class if your drawing units differ from mm.
- **Path**: Change the hardcoded path `C:/Users/Ivan/pdf-import/` to match your actual PDF storage location.
- **Encoding**: Change encoding from `cp1251` to `utf-8` if your AutoCAD version supports it.

## ⚠️ Limitations

- Only processes pages with `/MediaBox` defined. Pages without it are logged.
- Assumes PDFs are vector-based and suitable for import as blocks.
- Does not handle password-protected or encrypted PDFs.
- Generated LISP uses `._import` — ensure your AutoCAD version supports it (AutoCAD 2018+ recommended).

## 💡 Pro Tip

For best results:
- Pre-process PDFs to remove unnecessary pages.
- Use consistent page orientations.
- Place all PDFs in `pdf/` before running the script.

## 📜 License

This project is free to use and modify. No attribution required.
