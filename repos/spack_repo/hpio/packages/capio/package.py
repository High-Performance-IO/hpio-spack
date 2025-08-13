from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import * 

class Capio(CMakePackage):
    """
    CAPIO (Cross-Application Programmable I/O).
    Transparently inject streaming capabilities to 
    legacy file-based workflows!
    """

    homepage = "https://capio.hpc4ai.it"
    git      = "https://github.com/High-Performance-IO/capio.git"
    
    maintainers("marcoSanti", "GlassOfWhiskey")
    license("MIT")

    # Versions
    version("capio-v2", branch="capio-v2", preferred=True)  

    # Releases   
    version("1.0.0", tag="1.0.0")              

    # Variants
    variant("log", default=False, description="Enable CAPIO logger (and build CAPIO with debug symbols)")
    variant("tests", default=False, description="Build CAPIO tests suite")
    variant("debug", default=False, description="Build CAPIO in debug mode, with no optimization and debug symbols.")

    # Deps
    depends_on("cmake", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("capstone@4.0.2", type=("build", "run", "link"))
    depends_on("mpi", when="@1.0.0", type=("build", "run", "link"))

    # Build conflicts
    conflicts("platform=windows", msg="CAPIO only supports Linux")
    conflicts("platform=darwin", msg="CAPIO only supports Linux")
    

    def cmake_args(self) -> List[str]:
        target = "Debug" if "+debug" in self.spec else "Release"
        logger = "On" if "+log" in self.spec else "Off"
        tests  = "On" if "+tests" in self.spec else "Off"
        args = [
            f"-DCMAKE_BUILD_TYPE={target}",
            f"-DCAPIO_LOG={logger}",
            f"-DCAPIO_BUILD_TESTS={tests}"
        ]
        return args
    
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        import multiprocessing
        env.set('MAKEFLAGS', '-j{0}'.format(multiprocessing.cpu_count()))

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("LD_LIBRARY_PATH", self.spec["capio"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["capstone"].prefix.lib)