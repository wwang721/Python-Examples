# -*- mode: python -*-

block_cipher = None


a = Analysis(['getMouse.py'],
             pathex=['/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Users/wangwei/Documents/Python/getMouse'],
             binaries=[('/Users/wangwei/Documents/Python/Dynamic Link Library/lib/myDLL.so', 'lib')],
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
          name='getMouse',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
