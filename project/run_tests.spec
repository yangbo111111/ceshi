# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['run_tests.py',
              'config.py',
	      'conftest.py',
	       'E:\\project\\page\\__init__.py',
	       'E:\\project\\page\\systemmanage\\__init__.py',
	       'E:\\project\\page\\systemmanage\\sys_page.py',
	       'E:\\project\\test_case\\__init__.py',
               'E:\\project\\test_case\\\systemmanage\\__init__.py',
               'E:\\project\\test_case\\\systemmanage\\test_1_org.py',
               'E:\\project\\test_function\\__init__.py',
               'E:\\project\\test_function\\\systemmanage\\org_function.py',
	       'E:\\project\\test_function\\\systemmanage\\__init__.py',
	       'E:\\project\\test_function\\\systemmanage\\public_function.py',
	       ],
             pathex=['E:\\project'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='run_tests',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
