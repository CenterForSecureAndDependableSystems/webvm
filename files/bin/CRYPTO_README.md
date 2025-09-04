# Cryptography Tutorial

An interactive educational tool for learning essential cryptography concepts using hands-on OpenSSL commands.

## Overview

This tutorial provides a comprehensive introduction to cryptographic concepts through practical exercises using OpenSSL command-line tools. Students will learn by doing, executing real cryptographic operations and seeing immediate results.

## Requirements

### Software Requirements
- **Python 3.6+**: Required to run the tutorial framework
- **OpenSSL**: Required for all cryptographic operations
  - **Windows**: Download from [OpenSSL for Windows](https://slproweb.com/products/Win32OpenSSL.html) or install via Chocolatey: `choco install openssl`
  - **macOS**: Install via Homebrew: `brew install openssl`
  - **Linux**: Usually pre-installed, or install via package manager: `sudo apt-get install openssl`

### System Requirements
- Terminal/Command prompt access
- At least 50MB free disk space for sample files
- Internet connection for initial setup (if installing OpenSSL)

## Installation & Setup

1. **Verify Python Installation**:
   ```bash
   python --version
   # Should show Python 3.6 or higher
   ```

2. **Verify OpenSSL Installation**:
   ```bash
   openssl version
   # Should show OpenSSL version information
   ```

3. **Download Tutorial Files**:
   - Place `crypto_tutorial.py` and `CryptoAnswerKeyGenerator.py` in your desired directory
   - Ensure write permissions for creating sample files

4. **Run the Tutorial**:
   ```bash
   python crypto_tutorial.py
   ```

## Tutorial Structure

### 5 Comprehensive Lessons (50 Total Exercises)

1. **Hash Functions & Message Digests** (10 exercises)
   - MD5, SHA-1, SHA-256, SHA-512 hashing
   - File integrity verification
   - Hash sensitivity and avalanche effect
   - Binary vs hexadecimal output formats

2. **Symmetric Encryption with AES** (10 exercises)
   - AES-256-CBC encryption/decryption
   - Password-based vs key-based encryption
   - Base64 encoding for safe transmission
   - Key and IV generation
   - Encryption randomness demonstration

3. **Asymmetric Encryption with RSA** (10 exercises)
   - RSA key pair generation (1024, 2048, 4096-bit)
   - Public/private key operations
   - Message encryption and decryption
   - Password-protected private keys
   - Key size security implications

4. **Digital Signatures & Verification** (10 exercises)
   - Document signing with RSA + SHA-256
   - Signature verification
   - Tampering detection
   - Base64 signature encoding
   - Different hash algorithm signatures

5. **Certificates & Advanced Operations** (10 exercises)
   - Certificate Signing Requests (CSR)
   - Self-signed certificate creation
   - Certificate validation and inspection
   - Cryptographically secure random generation
   - Hybrid encryption (RSA + AES)

## Features

### Educational Focus
- **Hands-on Learning**: Execute real cryptographic commands
- **Immediate Feedback**: See results and verification instantly
- **Progressive Difficulty**: Build knowledge step-by-step
- **Real-world Applicable**: Learn industry-standard tools

### Student Tracking
- **Progress Codes**: Generated every 5 exercises for assignment submission
- **Assignment Keys**: Instructor-provided keys for grade tracking
- **Individual or Sequential**: Choose specific lessons or complete sequence
- **Automatic File Management**: Sample files created and managed automatically

### Instructor Support
- **Answer Key Generator**: `CryptoAnswerKeyGenerator.py` generates grading keys
- **Student Grouping**: Automatic assignment to groups for varied problem sets
- **CSV Export**: Easy integration with Learning Management Systems
- **Progress Tracking**: Monitor student completion with unique codes

## Sample Commands Covered

### Hash Functions
```bash
# Calculate different hash types
echo 'Hello World' | openssl md5
echo 'Hello World' | openssl sha256
openssl dgst -sha512 file.txt

# File integrity verification
openssl dgst -sha256 document.txt > document.hash
```

### Symmetric Encryption
```bash
# Password-based encryption
openssl enc -aes-256-cbc -in file.txt -out file.enc -k password

# Key-based encryption with explicit IV
openssl enc -aes-256-cbc -in file.txt -out file.enc -K $(cat key.hex) -iv $(cat iv.hex)

# Base64 encoding for safe transmission
openssl enc -aes-256-cbc -a -in file.txt -out file.b64 -k password
```

### Asymmetric Encryption
```bash
# Generate RSA key pair
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem

# Encrypt/decrypt with RSA
openssl pkeyutl -encrypt -pubin -inkey public.pem -in message.txt -out encrypted.bin
openssl pkeyutl -decrypt -inkey private.pem -in encrypted.bin -out decrypted.txt
```

### Digital Signatures
```bash
# Sign document
openssl dgst -sha256 -sign private.pem -out document.sig document.txt

# Verify signature
openssl dgst -sha256 -verify public.pem -signature document.sig document.txt
```

## Usage Examples

### For Students

1. **Complete All Lessons**:
   ```bash
   python crypto_tutorial.py
   # Choose 'all' from the menu
   ```

2. **Practice Specific Topic**:
   ```bash
   python crypto_tutorial.py
   # Choose lesson number (1-5)
   ```

3. **Resume from Checkpoint**:
   - Tutorial saves progress automatically
   - Progress codes generated every 5 exercises
   - Use codes for assignment submission

### For Instructors

1. **Generate Answer Keys**:
   ```bash
   python CryptoAnswerKeyGenerator.py
   # Creates assignment keys and student group mappings
   # Exports CSV for LMS integration
   ```

2. **Provide Assignment Keys**:
   - Each lesson requires instructor-provided key
   - Prevents unauthorized access to exercises
   - Enables proper grade tracking

3. **Monitor Progress**:
   - Students provide progress codes as proof of completion
   - Codes are cryptographically tied to specific exercises
   - Automatic verification against answer key

## File Structure

After running, the tutorial creates:

```
CryptoData/
├── secret.txt              # Sample secret message
├── message.txt             # Sample email content
├── financial.txt           # Sample financial data
├── personal.txt            # Sample personal information
├── document.txt            # Sample confidential document
├── plaintext.txt           # Sample plaintext for operations
├── data.txt                # Sample data file
├── *.enc                   # Encrypted files created during exercises
├── *.sig                   # Digital signature files
├── *.pem                   # RSA key files
├── *.hash                  # Hash verification files
└── *.b64                   # Base64 encoded files
```

## Security Considerations

### Educational Environment
- **Sample Data Only**: All exercises use non-sensitive sample files
- **Temporary Keys**: Cryptographic keys are generated for learning only
- **No Production Use**: Tutorial demonstrates concepts, not production security

### Best Practices Taught
- **Strong Key Generation**: Proper random key generation methods
- **Algorithm Selection**: When to use different cryptographic algorithms
- **Key Management**: Proper storage and protection of cryptographic keys
- **Verification Importance**: Always verify cryptographic operations

## Troubleshooting

### Common Issues

1. **OpenSSL Not Found**:
   ```
   Error: 'openssl' is not recognized as an internal or external command
   ```
   **Solution**: Install OpenSSL and ensure it's in your system PATH

2. **Permission Denied**:
   ```
   Error: Permission denied when creating files
   ```
   **Solution**: Run from a directory where you have write permissions

3. **Python Version**:
   ```
   Error: SyntaxError or module import issues
   ```
   **Solution**: Ensure Python 3.6+ is installed and being used

### Verification Commands

Test your setup:
```bash
# Test Python
python --version

# Test OpenSSL
openssl version

# Test file creation permissions
echo "test" > test.txt && rm test.txt
```

## Educational Outcomes

Upon completion, students will understand:

### Theoretical Concepts
- Hash functions and their properties
- Symmetric vs asymmetric encryption
- Digital signatures and authentication
- Public key infrastructure basics
- Cryptographic randomness importance

### Practical Skills
- OpenSSL command-line proficiency
- Real-world cryptographic tool usage
- File encryption and decryption
- Digital signature creation and verification
- Certificate management basics

### Security Awareness
- When to use different cryptographic techniques
- Common cryptographic mistakes to avoid
- Importance of key management
- Authentication vs encryption concepts

## Support and Contributions

### Getting Help
- Review this README for common issues
- Check OpenSSL documentation for command details
- Verify system requirements and installation

### Extending the Tutorial
The tutorial is designed to be extensible:
- Add new lessons by modifying the `load_lessons()` method
- Create additional verification methods as needed
- Expand sample files for more complex scenarios

## License and Usage

This educational tool is designed for classroom use and learning purposes. Students and instructors are free to use and modify for educational objectives.

---

**Happy Learning! 🔐**
