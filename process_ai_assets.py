#!/usr/bin/env python3
"""
Last Signal — AI Asset Processor
=================================
Drop your downloaded Higgsfield images into this folder and run this script.
It will detect, resize, and rename them for all platforms.

Usage:
    python3 process_ai_assets.py

The script looks for the MOST RECENT .jpg or .png files in this folder
and processes them into all required sizes.
"""
from PIL import Image, ImageDraw, ImageFont
import os
import glob
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

def find_latest_images(folder, count=6):
    """Find the most recent image files."""
    patterns = ['*.jpg', '*.jpeg', '*.png']
    files = []
    for pat in patterns:
        files.extend(glob.glob(os.path.join(folder, pat)))
    # Sort by modification time, newest first
    files.sort(key=os.path.getmtime, reverse=True)
    return files[:count]

def is_square(img):
    w, h = img.size
    return abs(w - h) < 50

def is_portrait(img):
    w, h = img.size
    return h > w * 1.3

def process_icon(path):
    """Process a square image as the app icon."""
    print(f"\n  Processing ICON: {os.path.basename(path)}")
    img = Image.open(path)
    print(f"    Source: {img.size[0]}x{img.size[1]}")

    # Remove rounded corners if present (crop to content)
    # For Higgsfield icons that include the rounded rect border
    w, h = img.size
    if w == h:
        # Check if there are dark corners (rounded icon border)
        # Crop inward slightly to remove any border artifacts
        margin = int(w * 0.02)
        img = img.crop((margin, margin, w - margin, h - margin))

    sizes = {
        "app-icon-1024.png": 1024,
        "app-icon-512.png": 512,
        "app-icon-180.png": 180,
        "app-icon-120.png": 120,
    }

    for name, sz in sizes.items():
        out = os.path.join(HERE, name)
        resized = img.resize((sz, sz), Image.LANCZOS)
        resized.save(out, "PNG")
        print(f"    Saved: {name} ({sz}x{sz})")

    # Keep full-res copy
    full_path = os.path.join(HERE, "app-icon-full.png")
    img.save(full_path, "PNG")
    print(f"    Saved: app-icon-full.png ({img.size[0]}x{img.size[1]})")

def process_splash(path):
    """Process a portrait image as the splash screen."""
    print(f"\n  Processing SPLASH: {os.path.basename(path)}")
    img = Image.open(path)
    print(f"    Source: {img.size[0]}x{img.size[1]}")

    # Standard mobile splash sizes
    sizes = {
        "splash-screen.png": (1080, 1920),
        "splash-screen-2x.png": (1242, 2208),  # iPhone 6+/7+/8+
        "splash-screen-3x.png": (1290, 2796),  # iPhone 14 Pro Max
    }

    for name, (tw, th) in sizes.items():
        # Resize maintaining aspect ratio, then crop to exact size
        src_ratio = img.size[0] / img.size[1]
        tgt_ratio = tw / th

        if src_ratio > tgt_ratio:
            # Source is wider — fit height, crop width
            new_h = th
            new_w = int(th * src_ratio)
        else:
            # Source is taller — fit width, crop height
            new_w = tw
            new_h = int(tw / src_ratio)

        resized = img.resize((new_w, new_h), Image.LANCZOS)

        # Center crop
        left = (new_w - tw) // 2
        top = (new_h - th) // 2
        cropped = resized.crop((left, top, left + tw, top + th))

        out = os.path.join(HERE, name)
        cropped.save(out, "PNG")
        print(f"    Saved: {name} ({tw}x{th})")

def main():
    print("=" * 50)
    print("Last Signal — AI Asset Processor")
    print("=" * 50)

    images = find_latest_images(HERE)

    if not images:
        print("\nNo images found! Download your Higgsfield images into this folder first.")
        print(f"  Folder: {HERE}")
        sys.exit(1)

    print(f"\nFound {len(images)} recent images:")
    for p in images:
        img = Image.open(p)
        ratio = "SQUARE" if is_square(img) else ("PORTRAIT" if is_portrait(img) else "OTHER")
        print(f"  {os.path.basename(p)} — {img.size[0]}x{img.size[1]} [{ratio}]")

    # Process each based on aspect ratio
    processed_icon = False
    processed_splash = False

    for p in images:
        img = Image.open(p)
        if is_square(img) and not processed_icon:
            process_icon(p)
            processed_icon = True
        elif is_portrait(img) and not processed_splash:
            process_splash(p)
            processed_splash = True

    if not processed_icon:
        print("\n  WARNING: No square image found for icon!")
        print("  Download the icon from Higgsfield (1:1 ratio) and re-run.")

    if not processed_splash:
        print("\n  WARNING: No portrait image found for splash!")
        print("  Download the splash from Higgsfield (9:16 ratio) and re-run.")

    print("\nDone!")

if __name__ == "__main__":
    main()
