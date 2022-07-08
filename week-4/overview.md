
# Executable file formats

Several executable formats exists. They are what let binaries run on systems.

## Executables

- macOS: Mach-O
- Linux: ELF
- Windows: PE32+ (PE)

## Libraries

- macOS: Dynamic Library (DyLib)
- Linux: Shared Object (SO)
- Windows: Dynamic-Link Library (DLL)

## API and ABI??

Application Programming Interfaces (APIs) exist so external apps know how to interface with the system.

Application Binary Interfaces (ABIs) exist so compilers can build interfaces that the lower system resources understand.

## DockCross

We can use DockCross which contains docker build environments to construct binaries for other systems. 
This eliminates the complexity associated with constructing tool chains needed to build binaries for specific targets.

GOLang is great because you don't need build tools for other systems installed - it can natively cross compile.

```bash
docker run --rm dockcross/windows-static-x64 > ./dockcross
./dockcross  bash -c '$CXX windows-mitre-ctf-challenge-2.cpp -o mitre-finale-part1'
```


### Sources

- https://github.com/dockcross/dockcross