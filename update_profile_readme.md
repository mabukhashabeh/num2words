# Instructions to Update GitHub Profile README

Your GitHub profile README is located at: `https://github.com/mabukhashabeh/mabukhashabeh`

## Steps to Update:

1. **Clone your profile repository** (if not already cloned):
   ```bash
   git clone https://github.com/mabukhashabeh/mabukhashabeh.git
   cd mabukhashabeh
   ```

2. **Update README.md** - Replace any references to:
   - `num2words` → `numwordify`
   - `numstowords` → `numwordify`
   - Old repository URL → New repository URL

3. **Example update** (if you have a projects section):
   ```markdown
   ## Projects
   
   - **[numwordify](https://github.com/mabukhashabeh/numwordify)** - A lightweight Python package for converting numbers to words in English and Arabic
     - PyPI: [numwordify](https://pypi.org/project/numwordify/)
     - Install: `pip install numwordify`
   ```

4. **Commit and push**:
   ```bash
   git add README.md
   git commit -m "Update project name to numwordify"
   git push
   ```

## Quick Find & Replace:

If you want to quickly update all references, you can use:
```bash
cd mabukhashabeh
sed -i '' 's/num2words/numwordify/g' README.md
sed -i '' 's/numstowords/numwordify/g' README.md
git add README.md
git commit -m "Update project name to numwordify"
git push
```
