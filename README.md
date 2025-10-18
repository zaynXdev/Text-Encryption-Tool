
# 🔐 Text Encryption Tool

A comprehensive **web-based text encryption application** built with **Python Flask** that implements multiple cryptographic algorithms for secure data transformation.  
This project demonstrates fundamental information security principles through a **user-friendly web interface**.


## 🎥 Video Demo

▶️ [Watch the Full Project Demonstration](https://drive.google.com/file/d/13Ug9rut9wfVIov9RKMGM5el1mnZ11khZ/view?usp=drive_link)



## ✨ Features

### 🔒 Multiple Encryption Algorithms
- **Caesar Cipher** – Classical substitution cipher  
- **Base64 Encoding** – Binary-to-text encoding  
- **AES-128 Encryption** – Military-grade symmetric encryption  
- **SHA-256 Hashing** – Cryptographic hash function  

### 🎯 User Experience
- Real-time Encryption/Decryption – Instant results  
- Separate Sections – Clear distinction between input, encrypted, and decrypted text  
- Copy to Clipboard – One-click copying for both encrypted and decrypted text  
- File Export – Download encrypted/decrypted text as files  
- Responsive Design – Works on desktop and mobile devices  
- Character Statistics – Real-time input/output length tracking  

### 🛡️ Security Features
- Input validation and sanitization  
- CORS protection  
- Security headers implementation  
- Secure random number generation  
- Error handling without information leakage  

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher  
- `pip` (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/zaynXdev/Text-Encryption-Tool.git
cd Text-Encryption-Tool

# Create virtual environment (Recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
````

Now open your browser and visit:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📚 Algorithm Details

### 🔤 Caesar Cipher

* **Type:** Substitution Cipher
* **Shift:** 3 positions forward
* **Security Level:** Basic (Educational)
* **Example:** `HELLO → KHOOR`

### 📄 Base64 Encoding

* **Type:** Binary-to-Text Encoding
* **Character Set:** A–Z, a–z, 0–9, +, /
* **Security Level:** None (Data representation)
* **Example:** `hello → aGVsbG8=`

### 🔐 AES Encryption

* **Algorithm:** AES-128 CBC Mode
* **Key Size:** 128-bit
* **Mode:** Cipher Block Chaining (CBC)
* **Security Level:** High (Industry Standard)
* **Features:** Random IV generation, PKCS7 padding

### 🔑 SHA-256 Hashing

* **Type:** Cryptographic Hash Function
* **Output:** 64-character hexadecimal
* **Properties:** One-way, collision-resistant
* **Security Level:** Very High
* **Example:** `hello → 2cf24dba5fb0a30e...`

---

## 🏗️ Project Structure

```
Text-Encryption-Tool/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── runtime.txt            # Python version specification
├── Procfile               # Deployment configuration
├── .env.example           # Environment variables template
├── test_simple.py         # Basic test suite
├── templates/             # HTML templates
│   ├── index.html         # Main application interface
│   └── index_debug.html   # Debug version with logging
└── static/
    └── style.css          # CSS styling and responsive design
```

---

## 🌐 API Endpoints

| Method | Endpoint   | Description                           |
| ------ | ---------- | ------------------------------------- |
| GET    | `/`        | Main application interface            |
| POST   | `/encrypt` | Encrypt text using selected algorithm |
| POST   | `/decrypt` | Decrypt previously encrypted text     |
| GET    | `/health`  | Health check endpoint                 |
| GET    | `/debug`   | Debug interface with logging          |

---

## 💻 Usage Examples

### Caesar Cipher

```python
Input: "HELLO WORLD"
Encrypted: "KHOOR ZRUOG"
Decrypted: "HELLO WORLD"
```

### Base64 Encoding

```python
Input: "hello"
Encoded: "aGVsbG8="
Decoded: "hello"
```

### AES Encryption

```python
Input: "secret message"
Encrypted: "U2FsdGVkX1+WvJw5t..."
Decrypted: "secret message"
```

### SHA-256 Hashing

```python
Input: "password123"
Hash: "ef92b778bafe771e..."
# Note: Hashing is one-way, cannot be decrypted
```

---

## 🔧 Development

### Running Tests

```bash
python test_simple.py
```

### Environment Configuration

Create a `.env` file for production:

```env
AES_ENCRYPTION_KEY=your_secure_16_byte_key_here
HASH_PEPPER=your_secret_pepper_here
FLASK_DEBUG=False
PORT=5000
```

### Code Structure Overview

```python
# Core encryption functions
def caesar_cipher_encrypt(text, shift=3)
def base64_encrypt(text)
def aes_encrypt(text)
def sha256_hash(text)

# Flask routes
@app.route('/encrypt', methods=['POST'])
@app.route('/decrypt', methods=['POST'])
```

---

## 🚀 Deployment

### Heroku Deployment

```bash
# Set up Heroku
heroku create your-app-name
git push heroku main

# Set environment variables
heroku config:set AES_ENCRYPTION_KEY=your_key
```

### PythonAnywhere

* Upload files to PythonAnywhere
* Configure virtual environment
* Set up WSGI configuration
* Reload web app

### Local Production

```bash
pip install gunicorn
gunicorn app:app
```

---

## 🛡️ Security Considerations

### Implemented Security Measures

✅ Input validation and length restrictions
✅ CORS protection for API endpoints
✅ Security headers (XSS protection, no-sniff)
✅ Secure random IV generation for AES
✅ Error handling without sensitive data exposure

### Production Recommendations

* Use HTTPS in production
* Store encryption keys in secure environment variables
* Implement rate limiting for API endpoints
* Regularly update dependencies
* Use proper logging and monitoring

---

## 📊 Performance

| Metric             | Description                  |
| ------------------ | ---------------------------- |
| Encryption Speed   | < 100ms for texts up to 10KB |
| Maximum Input Size | 10,000 characters            |
| Concurrent Users   | Limited by Flask dev server  |
| Memory Usage       | ~50MB                        |

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repository
2. Create a feature branch:

   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:

   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch:

   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Run in development mode
export FLASK_DEBUG=True
python app.py
```

---

## 🐛 Troubleshooting

### Common Issues

**1. ModuleNotFoundError: No module named 'Crypto'**

```bash
pip install pycryptodome
```

**2. CORS errors in browser**

* Ensure `flask-cors` is installed
* Check browser console for specific errors

**3. Encryption/Decryption not working**

* Verify algorithm selection
* Check browser network tab for failed requests
* Review Flask console for backend errors

### Getting Help

* Check the browser console for JavaScript errors
* Review Flask terminal output for Python errors
* Ensure all dependencies are installed
* Verify file paths and configurations

---


## 👨‍💻 Author

**Zayn**
GitHub: [@zaynXdev](https://github.com/zaynXdev)
Project: *Text Encryption Tool*

```


