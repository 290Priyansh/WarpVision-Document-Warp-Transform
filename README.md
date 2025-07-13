# 🔮 WarpVision - Document Warp Transform

Bring perspective to perfection!  
**WarpVision** is a lightweight OpenCV-based tool that allows you to correct the perspective of a 4-point selected area in an image — ideal for transforming scanned documents, game cards, ID cards, and more into perfectly aligned, top-down views.

---

## 📸 What It Does

Ever tried to capture a document with your camera but ended up with weird angles and skewed edges?  
**WarpVision** fixes that.

🌀 Select any **4 points** in an image (manually via mouse clicks)  
🔁 Automatically apply a **perspective transformation**  
📄 Extract a clean, flattened version of the selected region  
✅ Perfect for scanned papers, cards, and documents

> 🧭 **Important**: Click the four points **in order**:
> 1. Top-left  
> 2. Top-right  
> 3. Bottom-left  
> 4. Bottom-right

---

## 🛠️ Features

- 🖱️ Mouse-based point selection
- 📐 4-point perspective correction using OpenCV
- 🖼️ Instant preview of warped output
- ⚡ Lightweight and fast

---

## 🧠 How It Works

- The user clicks **4 points** on the source image using the mouse.
- These points are passed to OpenCV's `getPerspectiveTransform()`.
- The image is warped to a top-down view using `warpPerspective()`.

---

## 🧰 Tech Stack

- 🐍 Python
- 🎯 OpenCV
- 🔢 NumPy

---

## 🎬 Demo


> 


https://github.com/user-attachments/assets/44d7c935-37ac-4955-8adb-6ceb62a1ca31


---
## ✨ Use Cases

- Scanned Documents 📄
- Business Cards 💼
- Trading Cards ♠️
- Receipts 🧾
- Whiteboards 📋

---

## 🧙‍♂️ Inspired By

Inspired by real-world frustrations with off-angle document photos — and the power of OpenCV’s geometry magic.
