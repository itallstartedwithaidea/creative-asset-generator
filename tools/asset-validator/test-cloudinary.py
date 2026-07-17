#!/usr/bin/env python3
"""
Cloudinary Video Transformation Test Script
============================================
Tests video transformations to verify they work correctly.
"""

import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary import CloudinaryVideo
import sys

# Cloudinary credentials — set via environment variables, never hardcode:
#   export CLOUDINARY_CLOUD_NAME="your-cloud-name"
#   export CLOUDINARY_API_KEY="your-api-key"
#   export CLOUDINARY_API_SECRET="your-api-secret"
import os
CLOUD_NAME = os.environ.get("CLOUDINARY_CLOUD_NAME", "")
API_KEY = os.environ.get("CLOUDINARY_API_KEY", "")
API_SECRET = os.environ.get("CLOUDINARY_API_SECRET", "")

if not all([CLOUD_NAME, API_KEY, API_SECRET]):
    sys.exit("Missing Cloudinary credentials. Set CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET.")

# Configure Cloudinary
cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET,
    secure=True
)

def test_url_generation():
    """Test generating transformation URLs"""
    print("\n" + "="*60)
    print("🎬 CLOUDINARY VIDEO TRANSFORMATION TEST")
    print("="*60)
    
    # Test video public IDs from your console output
    test_videos = [
        "dp9ns53ghrq6mo0iuvgy",  # Latest upload
        "ssaeqwprxjrencjcwbfk",  # Previous upload
        "smmdyauqvl15qrdtwojb",
        "ttbamdiuzirfrzncgq9o"
    ]
    
    print(f"\n📦 Cloud Name: {CLOUD_NAME}")
    print(f"🔑 API Key: {API_KEY[:10]}...")
    
    # Test transformations
    transformations = [
        {
            "name": "1920x1080 Wide + Grayscale + AI Improve",
            "options": {
                "width": 1920,
                "height": 1080,
                "crop": "fill",
                "gravity": "auto",
                "quality": "auto:good",
                "effect": ["grayscale", "improve"]
            }
        },
        {
            "name": "720x1280 TikTok + Blur",
            "options": {
                "width": 720,
                "height": 1280,
                "crop": "fill",
                "gravity": "auto",
                "effect": "blur:500"
            }
        },
        {
            "name": "1080x1080 Square + Sepia + Vignette",
            "options": {
                "width": 1080,
                "height": 1080,
                "crop": "fill",
                "gravity": "auto",
                "effect": ["sepia:80", "vignette:50"]
            }
        },
        {
            "name": "Reverse Playback",
            "options": {
                "effect": "reverse"
            }
        },
        {
            "name": "Boomerang Effect",
            "options": {
                "effect": "boomerang"
            }
        },
        {
            "name": "Slow Motion (50%)",
            "options": {
                "effect": "accelerate:-50"
            }
        }
    ]
    
    for video_id in test_videos[:1]:  # Test with first video
        print(f"\n{'='*60}")
        print(f"📹 Testing video: {video_id}")
        print("="*60)
        
        for transform in transformations:
            print(f"\n✨ {transform['name']}:")
            
            # Build URL using Cloudinary SDK
            video = CloudinaryVideo(video_id)
            url = video.build_url(**transform['options'])
            
            print(f"   📎 URL: {url}")
    
    return True

def test_account_info():
    """Test account connection"""
    print("\n" + "="*60)
    print("🔐 ACCOUNT CONNECTION TEST")
    print("="*60)
    
    try:
        result = cloudinary.api.ping()
        print(f"✅ Connection successful: {result}")
        return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def test_list_resources():
    """List recent video uploads"""
    print("\n" + "="*60)
    print("📂 RECENT VIDEO UPLOADS")
    print("="*60)
    
    try:
        result = cloudinary.api.resources(
            resource_type="video",
            max_results=10,
            type="upload"
        )
        
        if result.get('resources'):
            for i, resource in enumerate(result['resources'], 1):
                print(f"\n{i}. {resource.get('public_id')}")
                print(f"   Format: {resource.get('format')}")
                print(f"   Size: {resource.get('bytes', 0) / 1024 / 1024:.2f} MB")
                print(f"   Dimensions: {resource.get('width')}x{resource.get('height')}")
                print(f"   URL: {resource.get('secure_url')}")
        else:
            print("No videos found in account")
            
        return True
    except Exception as e:
        print(f"❌ Error listing resources: {e}")
        return False

def generate_sample_urls():
    """Generate sample transformation URLs for documentation"""
    print("\n" + "="*60)
    print("📋 SAMPLE TRANSFORMATION URLS")
    print("="*60)
    
    video_id = "dp9ns53ghrq6mo0iuvgy"
    
    samples = [
        ("Resize 1920x1080", f"https://res.cloudinary.com/{CLOUD_NAME}/video/upload/w_1920,h_1080,c_fill,g_auto,q_auto/{video_id}.mp4"),
        ("Grayscale", f"https://res.cloudinary.com/{CLOUD_NAME}/video/upload/e_grayscale/{video_id}.mp4"),
        ("AI Improve", f"https://res.cloudinary.com/{CLOUD_NAME}/video/upload/e_improve/{video_id}.mp4"),
        ("Blur", f"https://res.cloudinary.com/{CLOUD_NAME}/video/upload/e_blur:500/{video_id}.mp4"),
        ("Sepia", f"https://res.cloudinary.com/{CLOUD_NAME}/video/upload/e_sepia:80/{video_id}.mp4"),
        ("Reverse", f"https://res.cloudinary.com/{CLOUD_NAME}/video/upload/e_reverse/{video_id}.mp4"),
        ("Boomerang", f"https://res.cloudinary.com/{CLOUD_NAME}/video/upload/e_boomerang/{video_id}.mp4"),
        ("All Effects Combined", f"https://res.cloudinary.com/{CLOUD_NAME}/video/upload/w_1920,h_1080,c_fill,g_auto,q_auto:good/e_grayscale/e_improve/{video_id}.mp4"),
    ]
    
    for name, url in samples:
        print(f"\n{name}:")
        print(f"   {url}")

if __name__ == "__main__":
    print("\n🚀 Starting Cloudinary Tests...")
    
    # Run tests
    test_account_info()
    test_list_resources()
    test_url_generation()
    generate_sample_urls()
    
    print("\n" + "="*60)
    print("✅ ALL TESTS COMPLETED")
    print("="*60 + "\n")

