
# SPACK Repository for High-Performance IO

This repository contains the [Spack](https://spack.readthedocs.io/) installation scripts for **CAPIO**, maintained by the High-Performance IO organization.

## 📦 Installation

1. **Add this repository to Spack**  
   ```bash
   spack repo add https://github.com/High-Performance-IO/hpio-spack.git
   ```

2. **Verify the repository was added successfully**  
   ```bash
   spack repo list
   ```
   Expected output should include an entry for `hpio`:
   ```
   [+] hpio       v2.2    ~/.spack/package_repos/.../repos/spack_repo/hpio
   [+] builtin    v2.2    ~/.spack/package_repos/.../repos/spack_repo/builtin
   ```
3. **Install CAPIO**  
   ```bash
   spack install capio
   ```
