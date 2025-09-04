# Linux Navigation Quiz - Troubleshooting FAQ

## 🚨 Common Issues & Solutions

### Installation & Setup Problems

#### ❌ "No module named 'tkinter'" Error
**Problem**: Quiz won't start, shows tkinter import error

**Solutions**:
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-tk

# CentOS/RHEL/Fedora
sudo yum install tkinter
# OR for newer versions:
sudo dnf install python3-tkinter

# Windows (if using native Python)
# Reinstall Python with "Add tkinter" option checked
# OR use WSL with above Linux commands

# macOS
brew install python-tk
```

**Test Fix**:
```python
python3 -c "import tkinter; print('tkinter works!')"
```

---

#### ❌ Quiz Creates No Files/Directories
**Problem**: QuizEnvironment folder not created, no file structure

**Possible Causes & Solutions**:

1. **Permission Issues**:
   ```bash
   # Check current directory permissions
   ls -la .
   
   # Ensure you can write here
   touch test_file && rm test_file
   
   # If permission denied, move to writable directory:
   cd ~/Desktop
   python linux_navigation_quiz.py
   ```

2. **Disk Space Issues**:
   ```bash
   # Check available space
   df -h .
   
   # Need at least 1MB free space
   # Clean up or move to different location
   ```

3. **Path Issues**:
   ```bash
   # Run from same directory as the quiz file
   ls linux_navigation_quiz.py  # Should exist
   python linux_navigation_quiz.py
   ```

---

#### ❌ "Assignment key not found" Error
**Problem**: Answer key generator says assignment key doesn't exist

**Solution**:
```bash
python NavigationQuizAnswerKeyGenerator.py
# Choose: 1. Set assignment key
# Enter the EXACT same key you gave students
# Case sensitive! "CS101_Week5" ≠ "cs101_week5"
```

**Prevention**: 
- Write down the exact assignment key when you create it
- Share the exact text with students (copy/paste, don't retype)

---

### Quiz Runtime Problems

#### ❌ Shell Commands Don't Work
**Problem**: Students type commands but get "command not found"

**Diagnosis**:
```bash
# Test basic commands outside quiz
which ls
which find
which cat
echo $PATH
```

**Solutions**:

1. **Not in Linux Environment**:
   ```bash
   # Windows users need WSL
   wsl --install
   # Then run quiz inside WSL
   ```

2. **PATH Issues**:
   ```bash
   # Add standard paths
   export PATH="/bin:/usr/bin:/usr/local/bin:$PATH"
   
   # Or run quiz with explicit paths
   python linux_navigation_quiz.py
   ```

3. **Wrong Shell**:
   ```bash
   # Ensure you're in bash/sh, not PowerShell
   bash
   python linux_navigation_quiz.py
   ```

---

#### ❌ Quiz Freezes or Becomes Unresponsive
**Problem**: GUI stops responding, can't click buttons

**Immediate Fix**:
```bash
# Force close and restart
Ctrl+C  # In terminal
# OR
killall python
python linux_navigation_quiz.py  # Restart
```

**Prevention**:
- Don't run multiple quiz instances simultaneously
- Close other heavy applications
- Ensure sufficient RAM (at least 512MB free)

**Recovery**:
```bash
# If quiz environment is corrupted
rm -rf QuizEnvironment/
python linux_navigation_quiz.py  # Regenerates clean environment
```

---

#### ❌ Wrong Verification Code Generated
**Problem**: Student gets different code than answer key shows

**Debugging Steps**:

1. **Check Student ID**:
   ```python
   # Must be EXACTLY the same
   # Answer key: "john.doe@university.edu"
   # Student entered: "John.Doe@university.edu"  # Wrong!
   ```

2. **Check Assignment Key**:
   ```python
   # Case sensitive!
   # Instructor set: "CS101_Week5"
   # Student entered: "cs101_week5"  # Wrong!
   ```

3. **Check Score**:
   ```bash
   # Re-run answer key generator
   python NavigationQuizAnswerKeyGenerator.py
   # Choose: 6. Test single student
   # Enter exact student ID and assignment key
   # Compare expected vs actual answers
   ```

4. **Environment Differences**:
   ```bash
   # Different operating systems might generate slightly different files
   # Ensure instructor and students use same OS type (all Linux/WSL)
   ```

---

### Answer Key Generator Problems

#### ❌ "Student list file not found"
**Problem**: Can't load student_list.txt

**Solution**:
```bash
# Create the file in same directory as answer key generator
ls student_list.txt  # Should exist

# File format (one email per line):
echo "student1@university.edu" > student_list.txt
echo "student2@university.edu" >> student_list.txt
echo "student3@university.edu" >> student_list.txt

# Test loading
python NavigationQuizAnswerKeyGenerator.py
# Choose: 2. Load student list
```

---

#### ❌ CSV Export Shows Wrong Scores
**Problem**: All students show 0 points or incorrect scores

**Check**:
1. **Answer Key Generated**: Must generate keys BEFORE validating codes
2. **Correct Assignment**: Ensure validating codes for correct assignment
3. **Code Format**: Codes should be 5 characters, uppercase hex (A3F7B)

**Fix**:
```bash
python NavigationQuizAnswerKeyGenerator.py
# 1. Set assignment key (correct one)
# 2. Load student list  
# 3. Generate answer keys
# 4. Save answer keys
# 5. Validate student codes (now should work)
```

---

### Performance Issues

#### ❌ Quiz Runs Very Slowly
**Problem**: Long delays between questions, slow shell response

**Solutions**:

1. **Close Other Programs**:
   ```bash
   # Close browsers, IDEs, etc.
   # Need at least 512MB RAM free
   ```

2. **Use Faster Storage**:
   ```bash
   # Run from SSD instead of USB drive
   # Move to local disk, not network drive
   ```

3. **Simplify Environment**:
   ```python
   # For testing, modify quiz to generate fewer files
   # In linux_navigation_quiz.py, reduce file counts
   ```

---

#### ❌ Answer Key Generation Takes Forever
**Problem**: Generating keys for large class (100+ students) is very slow

**Solutions**:
```bash
# Generate in smaller batches
# Split student_list.txt into groups of 25
split -l 25 student_list.txt batch_

# Generate keys for each batch
python NavigationQuizAnswerKeyGenerator.py
# Load batch_aa, generate, save as class1_keys.csv
# Load batch_ab, generate, save as class2_keys.csv
# etc.

# Combine CSV files later if needed
```

---

## 🔧 Advanced Troubleshooting

### Debug Mode for Quiz
Add this to beginning of `linux_navigation_quiz.py` for detailed output:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
DEBUG = True  # Add this line
```

### Verify File Generation
Test file structure creation:
```python
python3 -c "
from linux_navigation_quiz import *
generator = QuizEnvironmentGenerator('test@email.com', 'TestKey')
generator.create_quiz_environment()
print('Files created successfully')
"
```

### Manual Answer Checking
Verify specific student answers:
```bash
python3 -c "
from NavigationQuizAnswerKeyGenerator import *
generator = NavigationQuizAnswerKeyGenerator()
generator.set_assignment_key('YourKey')
answers = generator.get_correct_answers_for_student('student@email.com')
print(answers)
"
```

---

## 📞 Getting Help

### Self-Diagnosis Checklist
Before asking for help, try:

- [ ] Run `test_navigation_quiz.py` - does it pass all tests?
- [ ] Can you run basic Linux commands (`ls`, `cd`, `find`) in terminal?
- [ ] Is tkinter installed? (`python3 -c "import tkinter"`)
- [ ] Do you have write permissions in current directory?
- [ ] Are student ID and assignment key exactly the same (case-sensitive)?

### Log Files
Quiz creates log files for debugging:
```bash
# Check for error logs
ls *.log
cat quiz_errors.log  # If it exists

# Check system logs
dmesg | tail  # Linux system messages
```

### Test Environment
Create minimal test case:
```bash
# Test with simple student ID
python linux_navigation_quiz.py
# ID: test@test.com
# Key: TEST

# If this works, problem is with specific student data
# If this fails, problem is with installation/environment
```

---

## 🆘 Emergency Procedures

### During Class - Quiz Day Disasters

#### Crisis: Quiz Won't Start for Anyone
1. **Quick Fix**: Use paper-based backup questions
2. **Tech Fix**: Switch to instructor's machine, share screen
3. **Alternative**: Email quiz file to students, run individually

#### Crisis: Shell Commands Don't Work
1. **Immediate**: Switch to demonstration mode
2. **Workaround**: Instructor demonstrates commands on projector
3. **Recovery**: Students note answers, verify codes later

#### Crisis: Verification Codes All Wrong
1. **Don't Panic**: Students keep their final screens/screenshots
2. **Manual Verification**: Use answer key generator to check each student
3. **Grade Recovery**: Scores can be calculated from screenshots

### Data Recovery

#### Lost Answer Keys
```bash
# If you lose the CSV file, regenerate:
python NavigationQuizAnswerKeyGenerator.py
# Use same assignment key as before
# Load same student list
# Generate keys again (will be identical)
```

#### Corrupted Quiz Environment
```bash
# Start fresh for affected student:
rm -rf QuizEnvironment/
python linux_navigation_quiz.py
# Enter same student ID and assignment key
# Will regenerate identical environment
```

---

## 📋 Pre-Class Testing Protocol

### 1 Day Before Class:
- [ ] Test quiz on instructor machine
- [ ] Test quiz on student lab machine
- [ ] Generate answer keys for class
- [ ] Backup all files to cloud/USB

### 1 Hour Before Class:
- [ ] Test internet/network connectivity  
- [ ] Verify lab machines have Python + tkinter
- [ ] Test sample student login
- [ ] Have paper backup ready

### During Class:
- [ ] Start with one volunteer student
- [ ] Verify their environment generates correctly
- [ ] Check their shell commands work
- [ ] Confirm their code validates

---

## 🎯 Success Metrics

Quiz session is successful when:
- ✅ 95%+ students can start the quiz
- ✅ 90%+ students can complete all questions
- ✅ 100% verification codes validate correctly
- ✅ No data loss or corruption
- ✅ Students report learning Linux skills

---

**Remember: The quiz is designed to be robust, but when in doubt, test everything first! 🐧🔧**
