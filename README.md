# keep2anylist
Move Google Keep lists to AnyList

Uses two unofficial apps:
- https://github.com/kiwiz/gkeepapi
- https://github.com/codetheweb/anylist 

# Setup
Initialise submodules:

```bash
git submodule update --init
```

 (may need recursive flag too... check this)

# Libraries to install:
## Python
```bash
pip install ogpsoauth future python-dotenv requests "urllib3<2"
```