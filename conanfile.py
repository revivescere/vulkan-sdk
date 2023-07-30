from conan import ConanFile
from conan.tools.files import get

class VulkanSDK(ConanFile):
    name = "vulkan-sdk"
    version = "1.3.211.0"
    settings = "os", "compiler", "build_type", "arch"
    requires = (
        f"vulkan-headers/{version}",
        f"vulkan-loader/{version}",
        f"vulkan-validationlayers/{version}",
        # TODO: layer settings file
        # f"vulkan-extensionlayers/{version}",
        f"glslang/{version}",
        # f"vulkan-tools/{version}",
        f"spirv-headers/{version}",
        f"spirv-cross/{version}",
        f"spirv-tools/{version}",
        # f"shaderc/{version}",
        # f"volk/[^{version}]",
        # TODO: dxc - direct X compiler for linux and mac
        "glm/0.9.9.8",
        # "robin-hood-hashing/3.11.3",
        # "vulkan-docs/{version}",
        # "vulkan-profiles/{version}",
    )

    def config_options(self):
        # self.settings["vulkan-loader"].build_type = "RelWithDebInfo"
        # self.settings["vulkan-loader"].cpp_info.append(f"BUILD_DLL_VERSIONINFO={self.version}")
        # self.settings["vulkan-extensionlayers"].build_type = "RelWithDebInfo"
        # self.settings["shaderc"].cpp_info.extend([
        #     "CMAKE_DEBUG_POSTFIX=d",
        #     "SHADERC_SKIP_TESTS=ON",
        #     "SHADERC_ENABLE_SHARED_CRT=ON",
        #     "SHADERC_SKIP_COPYRIGHT_CHECK=ON",
        # ])
        # self.settings["robin-hood-hashing"].cpp_info.defines.append("RH_STANDALONE_PROJECT=OFF")
        # self.settings["vulkan-profiles"].cpp_info.defines.extend([
        #     "PROFILES_BUILD_TESTS=OFF",
        #     "REGENERATE_JSONCPP=OFF",
        #     "REGENERATE_PROFILES=OFF",
        #     "REGENERATE_LAYER=OFF",
        # ])
        pass

    def build_requirements(self):
        if self.settings.os == "Macos":
            self.requires("moltenvk/1.1.9")


