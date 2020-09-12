pip install -r requirements.txt
# Install tesseract via brew
if [[ -z $(which tesseract) ]]; then
    bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    brew install tesseract
fi