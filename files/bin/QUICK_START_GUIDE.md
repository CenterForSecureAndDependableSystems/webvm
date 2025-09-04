# Linux Navigation Quiz - Quick Start Guide

## 🚀 5-Minute Setup

### For Instructors

#### Step 1: Download & Test (2 minutes)
```bash
# Download the three main files:
# - linux_navigation_quiz.py
# - NavigationQuizAnswerKeyGenerator.py  
# - test_navigation_quiz.py

# Test everything works
python test_navigation_quiz.py
```

#### Step 2: Set Assignment Key (30 seconds)
```bash
python NavigationQuizAnswerKeyGenerator.py
# Choose: 1. Set assignment key
# Enter: YourClassName_Week5
# (e.g., CS101_Week5, CyberSec_LinuxQuiz, etc.)
```

#### Step 3: Create Student List (1 minute)
Create `student_list.txt`:
```
student1@university.edu
student2@university.edu
student3@university.edu
```

#### Step 4: Generate Answer Keys (1 minute)
```bash
python NavigationQuizAnswerKeyGenerator.py
# Choose: 2. Load student list
# Choose: 3. Generate answer keys  
# Choose: 4. Save answer keys (creates CSV file)
```

#### Step 5: Share with Students (30 seconds)
Give students:
- The quiz file: `linux_navigation_quiz.py`
- Assignment key: `YourClassName_Week5`
- Instructions: "Run the quiz and submit your verification code"

---

### For Students

#### Step 1: Download Quiz (30 seconds)
Get `linux_navigation_quiz.py` from your instructor

#### Step 2: Run Quiz (30 seconds)
```bash
python linux_navigation_quiz.py
```

#### Step 3: Enter Information (30 seconds)
- **Student ID**: your.email@university.edu
- **Assignment Key**: (provided by instructor)

#### Step 4: Complete Quiz (10-15 minutes)
- **Read question** in top window
- **Navigate files** in bottom shell window
- **Find answer** using Linux commands
- **Submit answer** and move to next question

#### Step 5: Submit Code (30 seconds)
- Get your **verification code** (e.g., "A3F7B")
- Submit to instructor/LMS for grading

---

## 🎯 What Students Will Do

### Example Question Flow:

**Question**: "What is the full path of file 'app89.py'?"

**Student Actions**:
```bash
# In the shell window:
$ ls
backup  config  documents  projects  temp

$ find . -name "app89.py"
./projects/mobile/app89.py

# Type in answer box: projects/mobile/app89.py
# Click Submit
```

**Result**: ✅ Correct! Moving to next question...

---

## 📝 Sample Questions Students Will See

1. **File Location**: "What is the full path of 'readme23.txt'?"
   - Use: `find . -name "readme23.txt"`

2. **File Counting**: "How many files are in the 'documents' directory?"
   - Use: `ls documents | wc -l`

3. **File Size**: "What is the size in bytes of 'backup34.tar'?"
   - Use: `ls -l backup/weekly/backup34.tar` or `du -b`

4. **Hidden Files**: "How many hidden files exist in total?"
   - Use: `find . -name ".*" -type f | wc -l`

5. **Content Reading**: "What is the content of 'secret_code.txt'?"
   - Use: `cat temp/secret_code.txt`

---

## 💡 Quick Tips

### For Instructors:
- **Test First**: Always run `test_navigation_quiz.py` before class
- **Unique Keys**: Use different assignment keys for different classes
- **Save CSV**: The answer key CSV imports easily into most LMS systems
- **Backup Codes**: Keep the generated answer key file safe

### For Students:
- **Use Tab**: Tab completion makes navigation faster
- **Try `ls -la`**: Shows hidden files and details
- **Use `find`**: Best tool for locating specific files
- **Read Carefully**: Questions ask for specific formats (paths vs names)
- **Practice Commands**: `cd`, `ls`, `find`, `cat`, `wc`, `du`

---

## ⚡ Command Cheat Sheet for Students

```bash
# Navigation
cd directory_name    # Enter directory
cd ..                # Go up one level
cd                   # Go to home
pwd                  # Show current location

# Listing Files
ls                   # List files
ls -la               # List all files with details
ls directory/        # List files in specific directory

# Finding Files
find . -name "filename"           # Find exact filename
find . -name "*.txt"              # Find all .txt files
find . -type f                    # Find all files
find . -name ".*"                 # Find hidden files

# Reading Files
cat filename         # Show file content
head filename        # Show first 10 lines
tail filename        # Show last 10 lines

# Counting & Measuring
wc -l filename       # Count lines in file
ls | wc -l          # Count files in directory
du -b filename       # Show file size in bytes
ls -l filename       # Show file details including size
```

---

## 🎯 Expected Time Investment

| Role | Setup Time | Quiz Time | Grading Time |
|------|------------|-----------|--------------|
| **Instructor** | 5 minutes | N/A | 2 minutes* |
| **Student** | 1 minute | 15 minutes | N/A |

*Grading is automated - just validate codes in CSV file

---

## ✅ Success Checklist

### Before Class (Instructor):
- [ ] `test_navigation_quiz.py` runs without errors
- [ ] Assignment key is set
- [ ] Student list is loaded
- [ ] Answer keys are generated and saved
- [ ] Students have quiz file and assignment key

### During Quiz (Student):
- [ ] Quiz starts and shows student ID correctly
- [ ] File structure is generated in QuizEnvironment/
- [ ] Shell commands work (ls, cd, find, etc.)
- [ ] Questions appear one by one
- [ ] Can submit answers and get feedback
- [ ] Receive verification code at end

### After Quiz (Instructor):
- [ ] Students submit their verification codes
- [ ] Codes can be validated using answer key generator
- [ ] Scores are correctly calculated from codes
- [ ] Grades are recorded in gradebook/LMS

---

## 🚨 Emergency Contacts

If something goes wrong during quiz time:

1. **Quiz won't start**: Check Python and tkinter installation
2. **No file structure**: Ensure write permissions in directory  
3. **Shell not working**: Verify Linux/WSL environment
4. **Wrong verification code**: Re-run quiz with same student ID

**For urgent issues**: Check the full troubleshooting guide!

---

**Ready to assess Linux skills authentically! 🐧📊**
