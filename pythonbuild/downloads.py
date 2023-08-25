# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

DOWNLOADS = {
    "autoconf": {
        "url": "https://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz",
        "size": 1927468,
        "sha256": "954bd69b391edc12d6a4a51a2dd1476543da5c6bbf05a95b59dc0dd6fd4c2969",
        "version": "2.69",
    },
    # 6.0.19 is the last version licensed under the Sleepycat license.
    "bdb": {
        "url": "https://ftp.osuosl.org/pub/blfs/conglomeration/db/db-6.0.19.tar.gz",
        "size": 36541923,
        "sha256": "2917c28f60903908c2ca4587ded1363b812c4e830a5326aaa77c9879d13ae18e",
        "version": "6.0.19",
        "library_names": ["db"],
        "licenses": ["Sleepycat"],
        "license_file": "LICENSE.bdb.txt",
    },
    "binutils": {
        "url": "https://ftp.gnu.org/gnu/binutils/binutils-2.41.tar.xz",
        "size": 26765692,
        "sha256": "ae9a5789e23459e59606e6714723f2d3ffc31c03174191ef0d015bdf06007450",
        "version": "2.41",
    },
    "bzip2": {
        "url": "https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz",
        "size": 810029,
        "sha256": "ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269",
        "version": "1.0.8",
        "library_names": ["bz2"],
        "licenses": ["bzip2-1.0.6"],
        "license_file": "LICENSE.bzip2.txt",
    },
    "cpython-3.8": {
        "url": "https://www.python.org/ftp/python/3.8.17/Python-3.8.17.tar.xz",
        "size": 20696584,
        "sha256": "2e54b0c68191f16552f6de2e97a2396540572a219f6bbb28591a137cecc490a9",
        "version": "3.8.17",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp38",
    },
    "cpython-3.9": {
        "url": "https://www.python.org/ftp/python/3.9.18/Python-3.9.18.tar.xz",
        "size": 19673928,
        "sha256": "01597db0132c1cf7b331eff68ae09b5a235a3c3caa9c944c29cac7d1c4c4c00a",
        "version": "3.9.18",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp39",
    },
    "cpython-3.10": {
        "url": "https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tar.xz",
        "size": 19663088,
        "sha256": "5c88848668640d3e152b35b4536ef1c23b2ca4bd2c957ef1ecbb053f571dd3f6",
        "version": "3.10.13",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp310",
    },
    "cpython-3.11": {
        "url": "https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tar.xz",
        "size": 19954828,
        "sha256": "2f0e409df2ab57aa9fc4cbddfb976af44e4e55bf6f619eee6bc5c2297264a7f6",
        "version": "3.11.4",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp311",
    },
    "expat": {
        "url": "https://github.com/libexpat/libexpat/releases/download/R_2_5_0/expat-2.5.0.tar.xz",
        "size": 460560,
        "sha256": "ef2420f0232c087801abf705e89ae65f6257df6b7931d37846a193ef2e8cdcbe",
        "version": "2.5.0",
        "library_names": ["expat"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.expat.txt",
    },
    "inputproto": {
        "url": "https://www.x.org/archive/individual/proto/inputproto-2.3.2.tar.gz",
        "size": 244334,
        "sha256": "10eaadd531f38f7c92ab59ef0708ca195caf3164a75c4ed99f0c04f2913f6ef3",
        "version": "2.3.2",
    },
    "jom-windows-bin": {
        "url": "http://download.qt.io/official_releases/jom/jom_1_1_3.zip",
        "size": 1213852,
        "sha256": "128fdd846fe24f8594eed37d1d8929a0ea78df563537c0c1b1861a635013fff8",
        "version": "1.1.3",
    },
    "kbproto": {
        "url": "https://www.x.org/archive/individual/proto/kbproto-1.0.7.tar.gz",
        "size": 325858,
        "sha256": "828cb275b91268b1a3ea950d5c0c5eb076c678fdf005d517411f89cc8c3bb416",
        "version": "1.0.7",
    },
    # 20221009-3.1 fails to build on musl due to an includes issue.
    "libedit": {
        "url": "https://thrysoee.dk/editline/libedit-20210910-3.1.tar.gz",
        "size": 524722,
        "sha256": "6792a6a992050762edcca28ff3318cdb7de37dccf7bc30db59fcd7017eed13c5",
        "version": "20210910-3.1",
        "library_names": ["edit"],
        "licenses": ["BSD-3-Clause"],
        "license_file": "LICENSE.libedit.txt",
    },
    # libffi 3.4 has trouble building with musl due to Linux headers wonkiness.
    "libffi": {
        "url": "https://github.com/libffi/libffi/releases/download/v3.3/libffi-3.3.tar.gz",
        "size": 1305466,
        "sha256": "72fba7922703ddfa7a028d513ac15a85c8d54c8d67f55fa5a4802885dc652056",
        "version": "3.3",
        "library_names": ["ffi"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libffi.txt",
    },
    "libpthread-stubs": {
        "url": "https://www.x.org/archive/individual/lib/libpthread-stubs-0.1.tar.gz",
        "size": 301448,
        "sha256": "f8f7ca635fa54bcaef372fd5fd9028f394992a743d73453088fcadc1dbf3a704",
        "version": "0.1",
    },
    "libX11": {
        "url": "https://www.x.org/archive/individual/lib/libX11-1.6.8.tar.gz",
        "size": 3144482,
        "sha256": "69d1a27cba722dca897198a23fa8d3cad3ec0c715e00205ea4398ec68a4258a5",
        "version": "1.6.8",
        "library_names": ["X11", "X11-xcb"],
        "licenses": ["MIT", "X11"],
        "license_file": "LICENSE.libX11.txt",
    },
    "libXau": {
        "url": "https://www.x.org/releases/individual/lib/libXau-1.0.7.tar.gz",
        "size": 349278,
        "sha256": "cbb81b4ba0f585faac8b9914b0bdbef6e0ef886a30c70d6584e2b30efeda9ac4",
        "version": "1.0.7",
        "library_names": ["Xau"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libXau.txt",
    },
    "libxcb": {
        "url": "https://xcb.freedesktop.org/dist/libxcb-1.13.1.tar.gz",
        "size": 636748,
        "sha256": "f09a76971437780a602303170fd51b5f7474051722bc39d566a272d2c4bde1b5",
        "version": "1.13.1",
        "library_names": ["xcb"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libxcb.txt",
    },
    "llvm-14-x86_64-linux": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20220508/llvm-14.0.3+20220508-gnu_only-x86_64-unknown-linux-gnu.tar.zst",
        "size": 158614671,
        "sha256": "04cb77c660f09df017a57738ae9635ef23a506024789f2f18da1304b45af2023",
        "version": "14.0.3+20220508",
    },
    "llvm-16-x86_64-linux": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20230506/llvm-16.0.3+20230506-gnu_only-x86_64-unknown-linux-gnu.tar.zst",
        "size": 226142860,
        "sha256": "5fbddd82919fb855684aa79c4f862248e1ceda9334259062803965e5d3d264d4",
        "version": "16.0.3+2023506",
    },
    "llvm-aarch64-macos": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20230506/llvm-16.0.3+20230506-aarch64-apple-darwin.tar.zst",
        "size": 116375025,
        "sha256": "f8353cbeadc4be9d83a2b0ae1dc48efe80a4700dac5bd6bdc8058b9144336479",
        "version": "16.0.3+20230506",
    },
    "llvm-x86_64-macos": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20230506/llvm-16.0.3+20230506-x86_64-apple-darwin.tar.zst",
        "size": 123709633,
        "sha256": "59b9d16f27383444ec458eb116778e871c2e23e92f6704c319f7ab5747a3e26e",
        "version": "16.0.3+20230506",
    },
    "m4": {
        "url": "https://ftp.gnu.org/gnu/m4/m4-1.4.19.tar.xz",
        "size": 1654908,
        "sha256": "63aede5c6d33b6d9b13511cd0be2cac046f2e70fd0a07aa9573a04a82783af96",
        "version": "1.4.19",
    },
    "mpdecimal": {
        "url": "https://www.bytereef.org/software/mpdecimal/releases/mpdecimal-2.5.1.tar.gz",
        "size": 2584021,
        "sha256": "9f9cd4c041f99b5c49ffb7b59d9f12d95b683d88585608aa56a6307667b2b21f",
        "version": "2.5.1",
        "library_names": ["mpdec"],
        "licenses": ["BSD-2-Clause"],
        "license_file": "LICENSE.mpdecimal.txt",
    },
    "musl": {
        "url": "https://musl.libc.org/releases/musl-1.2.4.tar.gz",
        "size": 1063758,
        "sha256": "7a35eae33d5372a7c0da1188de798726f68825513b7ae3ebe97aaaa52114f039",
        "version": "1.2.4",
    },
    "ncurses": {
        "url": "https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.3.tar.gz",
        "size": 3583550,
        "sha256": "97fc51ac2b085d4cde31ef4d2c3122c21abc217e9090a43a30fc5ec21684e059",
        "version": "6.3",
        "library_names": ["ncurses", "ncursesw", "panel", "panelw"],
        "licenses": ["X11"],
        "license_file": "LICENSE.ncurses.txt",
    },
    "openssl": {
        "url": "https://www.openssl.org/source/openssl-1.1.1v.tar.gz",
        "size": 9893443,
        "sha256": "d6697e2871e77238460402e9362d47d18382b15ef9f246aba6c7bd780d38a6b0",
        "version": "1.1.1v",
        "library_names": ["crypto", "ssl"],
        "licenses": ["OpenSSL"],
        "license_file": "LICENSE.openssl.txt",
    },
    "nasm-windows-bin": {
        "url": "https://github.com/python/cpython-bin-deps/archive/nasm-2.11.06.tar.gz",
        "size": 384826,
        "sha256": "8af0ae5ceed63fa8a2ded611d44cc341027a91df22aaaa071efedc81437412a5",
        "version": "2.11.06",
    },
    "patchelf": {
        "url": "https://github.com/NixOS/patchelf/releases/download/0.13.1/patchelf-0.13.1.tar.bz2",
        "size": 173598,
        "sha256": "39e8aeccd7495d54df094d2b4a7c08010ff7777036faaf24f28e07777d1598e2",
        "version": "0.13.1",
    },
    "pip": {
        "url": "https://files.pythonhosted.org/packages/50/c2/e06851e8cc28dcad7c155f4753da8833ac06a5c704c109313b8d5a62968a/pip-23.2.1-py3-none-any.whl",
        "size": 2086091,
        "sha256": "7ccf472345f20d35bdc9d1841ff5f313260c2c33fe417f48c30ac46cccabf5be",
        "version": "23.2.1",
    },
    "readline": {
        "url": "https://ftp.gnu.org/gnu/readline/readline-8.2.tar.gz",
        "size": 3043952,
        "sha256": "3feb7171f16a84ee82ca18a36d7b9be109a52c04f492a053331d7d1095007c35",
        "version": "8.2",
        "library_names": ["readline"],
        "licenses": ["GPL-3.0-only"],
        "license_file": "LICENSE.readline.txt",
    },
    "setuptools": {
        "url": "https://files.pythonhosted.org/packages/4f/ab/0bcfebdfc3bfa8554b2b2c97a555569c4c1ebc74ea288741ea8326c51906/setuptools-68.1.2-py3-none-any.whl",
        "size": 805130,
        "sha256": "3d8083eed2d13afc9426f227b24fd1659489ec107c0e86cec2ffdde5c92e790b",
        "version": "68.1.2",
    },
    # Remember to update verify_distribution.py when version changed.
    "sqlite": {
        "url": "https://www.sqlite.org/2023/sqlite-autoconf-3430000.tar.gz",
        "size": 3178199,
        "sha256": "49008dbf3afc04d4edc8ecfc34e4ead196973034293c997adad2f63f01762ae1",
        "version": "3430000",
        "actual_version": "3.43.0.0",
        "library_names": ["sqlite3"],
        "licenses": [],
        "license_file": "LICENSE.sqlite.txt",
        "license_public_domain": True,
    },
    "strawberryperl": {
        "url": "http://strawberryperl.com/download/5.28.1.1/strawberry-perl-5.28.1.1-32bit-portable.zip",
        "size": 143242779,
        "sha256": "8b15c7c9574989568254a7859e473b7d5f68a1145d2e4418036600a81b13805c",
        "version": "5.28.1.1",
    },
    "tcl": {
        "url": "https://prdownloads.sourceforge.net/tcl/tcl8.6.12-src.tar.gz",
        "size": 10353486,
        "sha256": "26c995dd0f167e48b11961d891ee555f680c175f7173ff8cb829f4ebcde4c1a6",
        "version": "8.6.12",
        "library_names": ["tcl8.6"],
        "licenses": ["TCL"],
        "license_file": "LICENSE.tcl.txt",
    },
    "tix": {
        "url": "https://github.com/python/cpython-source-deps/archive/tix-8.4.3.6.tar.gz",
        "size": 1836451,
        "sha256": "f7b21d115867a41ae5fd7c635a4c234d3ca25126c3661eb36028c6e25601f85e",
        "version": "8.4.3.6",
        "licenses": ["TCL"],
        "license_file": "LICENSE.tix.txt",
    },
    "tk": {
        "url": "https://prdownloads.sourceforge.net/tcl/tk8.6.12-src.tar.gz",
        "size": 4515393,
        "sha256": "12395c1f3fcb6bed2938689f797ea3cdf41ed5cb6c4766eec8ac949560310630",
        "version": "8.6.12",
        "library_names": ["tk8.6"],
        "licenses": ["TCL"],
        "license_file": "LICENSE.tcl.txt",
    },
    "tk-windows-bin": {
        "url": "https://github.com/python/cpython-bin-deps/archive/e3c3e9a2856124aa32b608632a52742d479eb7a9.tar.gz",
        "size": 6787654,
        "sha256": "01ad9c663659224e075d487cbc33ea2fed7a225593965b79bed92ca7f79b676f",
        "version": "8.6.12",
        "git_commit": "e3c3e9a2856124aa32b608632a52742d479eb7a9",
    },
    "uuid": {
        "url": "https://sourceforge.net/projects/libuuid/files/libuuid-1.0.3.tar.gz",
        "size": 318256,
        "sha256": "46af3275291091009ad7f1b899de3d0cea0252737550e7919d17237997db5644",
        "version": "1.0.3",
        "library_names": ["uuid"],
        "licenses": ["BSD-3-Clause"],
        "license_file": "LICENSE.libuuid.txt",
    },
    "x11-util-macros": {
        "url": "https://www.x.org/archive/individual/util/util-macros-1.19.2.tar.gz",
        "size": 103001,
        "sha256": "9225c45c3de60faf971979a55a5536f3562baa4b6f02246c23e98ac0c09a75b7",
        "version": "1.19.2",
    },
    "xcb-proto": {
        "url": "https://www.x.org/archive/individual/proto/xcb-proto-1.14.1.tar.gz",
        "size": 194674,
        "sha256": "85cd21e9d9fbc341d0dbf11eace98d55d7db89fda724b0e598855fcddf0944fd",
        "version": "1.14.1",
    },
    "xextproto": {
        "url": "https://www.x.org/archive/individual/proto/xextproto-7.3.0.tar.gz",
        "size": 290814,
        "sha256": "1b1bcdf91221e78c6c33738667a57bd9aaa63d5953174ad8ed9929296741c9f5",
        "version": "7.3.0",
    },
    "xorgproto": {
        "url": "https://www.x.org/archive/individual/proto/xorgproto-2019.1.tar.gz",
        "size": 1119813,
        "sha256": "38ad1d8316515785d53c5162b4b7022918e03c11d72a5bd9df0a176607f42bca",
        "version": "2019.1",
    },
    "xproto": {
        "url": "https://www.x.org/archive/individual/proto/xproto-7.0.31.tar.gz",
        "size": 367979,
        "sha256": "6d755eaae27b45c5cc75529a12855fed5de5969b367ed05003944cf901ed43c7",
        "version": "7.0.31",
    },
    "xtrans": {
        "url": "https://www.x.org/archive/individual/lib/xtrans-1.4.0.tar.gz",
        "size": 225941,
        "sha256": "48ed850ce772fef1b44ca23639b0a57e38884045ed2cbb18ab137ef33ec713f9",
        "version": "1.4.0",
    },
    "xz": {
        "url": "https://tukaani.org/xz/xz-5.2.12.tar.gz",
        "size": 2190541,
        "sha256": "61bda930767dcb170a5328a895ec74cab0f5aac4558cdda561c83559db582a13",
        "version": "5.2.12",
        "library_names": ["lzma"],
        # liblzma is in the public domain. Other parts of code have licenses. But
        # we only use liblzma.
        "licenses": [],
        "license_file": "LICENSE.liblzma.txt",
        "license_public_domain": True,
    },
    "zlib": {
        "url": "https://zlib.net/fossils/zlib-1.2.13.tar.gz",
        "size": 1497445,
        "sha256": "b3a24de97a8fdbc835b9833169501030b8977031bcb54b3b3ac13740f846ab30",
        "version": "1.2.13",
        "library_names": ["z"],
        "licenses": ["Zlib"],
        "license_file": "LICENSE.zlib.txt",
    },
}
