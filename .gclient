solutions = [
  {
    "name": "src",
    "url": "https://github.com/chromium/chromium.git",
    "managed": False,
    "custom_deps": {},
    "custom_vars": {
      "checkout_android_native_support": True,
      "checkout_webview": True,
      "checkout_webrtc": True,
      "checkout_vulkan": True,
      "vulkan_validation_layers_url": "https://github.com/KhronosGroup/Vulkan-ValidationLayers.git",
      "vulkan_tools_url": "https://github.com/KhronosGroup/Vulkan-Tools.git",
      "vulkan_headers_url": "https://github.com/KhronosGroup/Vulkan-Headers.git",
      "vulkan_utility_libraries_url": "https://github.com/KhronosGroup/Vulkan-Utility-Libraries.git",
      "vulkan_memory_allocator_url": "https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator.git"
    },
  },
]
target_os = ["android"]