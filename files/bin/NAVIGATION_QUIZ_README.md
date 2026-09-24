# Linux Navigation Quiz System

An interactive assessment tool that tests students' Linux file system navigation skills using a dual-window interface with live shell access and auto-generated file structures.

## 🎯 Overview

This quiz system creates unique file structures for each student and tests their ability to navigate, search, and analyze files using Linux commands. Students interact with a real shell while answering questions in a separate instruction window.

## 🏗️ System Architecture

### Student Interface: `linux_navigation_quiz.py`
- **Dual Window GUI**: Instructions/questions on top, live shell on bottom
- **Auto-generated Environment**: Unique file structure per student
- **Interactive Shell**: Real Linux commands with immediate feedback
- **Verification Codes**: 5-character hex codes for grade submission

### Instructor Tools: `NavigationQuizAnswerKeyGenerator.py`
- **Answer Key Generation**: Creates grading keys for all students
- **Code Validation**: Verifies student submission codes
- **CSV Export**: Easy LMS integration
- **Student Management**: Handles class lists and group assignments

## 📁 File Structure Generation

Each student receives a unique file system based on their ID:

```
QuizEnvironment/
├── documents/
│   ├── reports/
│   │   └── report47.doc
│   ├── drafts/
│   └── readme23.txt
├── projects/
│   ├── web/
│   │   └── index12.html
│   └── mobile/
│       └── app89.py
├── backup/
│   ├── weekly/
│   │   └── backup34.tar
│   └── daily/
│       └── size_test.log
├── config/
│   ├── config56.conf
│   └── .hidden_config
├── temp/
│   ├── notes78.txt
│   └── secret_code.txt
└── .profile
```

**Key Features:**
- **Deterministic Generation**: Same student ID always creates same structure
- **Random Elements**: File names, sizes, and content vary per student
- **Hidden Files**: Tests understanding of `.` files and `ls -a`
- **Nested Directories**: Requires navigation skills
- **Variable Content**: Different file sizes and specific content for targeted questions

## 🎯 Question Types

The quiz generates 8 different types of questions:

1. **File Path Location**: "What is the full path of file 'readme23.txt'?"
2. **File Counting**: "How many files are in the 'documents' directory?"
3. **File Size Analysis**: "What is the size in bytes of 'size_test.log'?"
4. **Hidden File Detection**: "How many hidden files are in the entire structure?"
5. **Content Extraction**: "What is the content of 'secret_code.txt'?"
6. **Extension Analysis**: "How many .txt files exist in total?"
7. **Largest File ID**: "What is the name of the largest file?"
8. **Directory Comparison**: "Which directory contains the most files?"

## 💻 Student Experience

### GUI Interface
```
┌─ Quiz Instructions ─────────────────────────────────┐
│ Question 1:                                         │
│                                                     │
│ What is the full path of the file named 'app89.py'?│
│                                                     │
│ Your Answer: [projects/mobile/app89.py    ] Submit │
│ Question 1/8                                        │
└─────────────────────────────────────────────────────┘
┌─ Live Shell (Navigate Here) ────────────────────────┐
│ $ ls                                                │
│ backup  config  documents  projects  temp          │
│ $ cd projects                                       │
│ $ ls -la                                            │
│ drwxr-xr-x 4 user user  128 Sep  2 14:30 .         │
│ drwxr-xr-x 3 user user   96 Sep  2 14:30 ..        │
│ drwxr-xr-x 2 user user   64 Sep  2 14:30 mobile    │
│ drwxr-xr-x 2 user user   64 Sep  2 14:30 web       │
│ $ cd mobile                                         │
│ $ ls                                                │
│ app89.py                                            │
│ $ _                                                 │
│                                                     │
│ [Clear Shell] [Show Hint] [Reset to Quiz Directory]│
└─────────────────────────────────────────────────────┘
```

### Learning Process
1. **Read Question**: Understand what information is needed
2. **Navigate Shell**: Use `cd`, `ls`, `find`, etc. to explore
3. **Gather Information**: Use `cat`, `wc`, `du`, etc. to get data
4. **Submit Answer**: Enter findings in answer field
5. **Get Feedback**: Immediate correct/incorrect notification

## 🔑 Verification System

### Code Generation
- **Student Data**: ID + Assignment Key + Score + Question Count
- **Answer Pattern**: Which questions were answered correctly
- **MD5 Hash**: First 5 hex characters = verification code
- **Example**: Student gets 6/8 correct → Code: "A3F7B"

### Security Features
- **Unique Per Student**: Same structure but different answers
- **Score Dependent**: Different codes for different scores
- **Tamper Resistant**: Cannot guess codes without actual navigation
- **Instructor Validation**: Answer key allows score verification

## 🚀 Setup & Installation

### Requirements
- **Python 3.6+** with tkinter (GUI support)
- **Linux/WSL Environment** for shell commands
- **Standard Linux Tools**: ls, find, cat, wc, du, etc.

### Quick Start

1. **Download Files**:
   ```bash
   # Main quiz program
   linux_navigation_quiz.py
   
   # Answer key generator
   NavigationQuizAnswerKeyGenerator.py
   
   # Test script
   test_navigation_quiz.py
   ```

2. **Test Installation**:
   ```bash
   python test_navigation_quiz.py
   ```

3. **Generate Answer Keys** (Instructors):
   ```bash
   python NavigationQuizAnswerKeyGenerator.py
   ```

4. **Run Quiz** (Students):
   ```bash
   python linux_navigation_quiz.py
   ```

## 👨‍🏫 Instructor Workflow

### 1. Setup Assignment
```bash
python NavigationQuizAnswerKeyGenerator.py
# Choose: 1. Set assignment key
# Enter: NavQuiz_Week5
```

### 2. Prepare Student List
Create `student_list.txt`:
```
john.doe@university.edu
jane.smith@university.edu
bob.johnson@university.edu
```

### 3. Generate Answer Keys
```bash
# 2. Load student list
# 3. Generate answer keys
# 4. Save answer keys
```

### 4. Distribution
- Give students the assignment key: `NavQuiz_Week5`
- Students run quiz and submit verification codes
- Use saved CSV file to validate codes and assign grades

### 5. Grading
```bash
# 5. Validate student codes
# Enter student ID and their submitted code
# Get automatic score verification
```

## 👨‍🎓 Student Workflow

### 1. Start Quiz
```bash
python linux_navigation_quiz.py
# Enter student ID: john.doe@university.edu
# Enter assignment key: NavQuiz_Week5
```

### 2. Navigate & Answer
- Use shell window to explore file structure
- Find information requested in questions
- Submit answers in instruction window

### 3. Complete & Submit
- Get final verification code (e.g., "A3F7B")
- Submit code to instructor/LMS for grading

## 🔧 Technical Details

### File Generation Algorithm
```python
# Deterministic randomization
seed = hash(student_id + assignment_key)
random.seed(seed)

# Generate unique filenames
filename = base_name + str(random.randint(1, 99)) + extension

# Modify content with student info
content = base_content + f"\nStudent: {student_id}\nGenerated: {timestamp}"
```

### Question Generation
- **Deterministic**: Same student always gets same questions
- **Varied Answers**: Different file structures = different answers
- **Skill Testing**: Questions require multiple Linux commands
- **Progressive Difficulty**: From simple `ls` to complex `find` operations

### Verification Algorithm
```python
verification_data = f"{student_id}:{assignment_key}:{score}:{total_questions}"
for correct in answer_pattern:
    verification_data += f":{correct}"
    
code = hashlib.md5(verification_data.encode()).hexdigest()[:5].upper()
```

## 📊 Assessment Features

### Skills Tested
- **Basic Navigation**: `cd`, `ls`, `pwd`
- **File Listing**: `ls -la`, `ls -R`
- **File Search**: `find` command with various options
- **Content Reading**: `cat`, `head`, `tail`
- **File Analysis**: `wc`, `du`, `stat`
- **Pattern Matching**: Wildcards and regular expressions

### Grading Support
- **Automatic Scoring**: 8 questions, each worth 12.5%
- **Verification Codes**: Cryptographic proof of completion
- **CSV Export**: Ready for LMS import
- **Individual Tracking**: Unique codes per student
- **Cheat Prevention**: Cannot fake navigation without actual skills

## 🔒 Security & Academic Integrity

### Prevents Cheating
- **Unique Environments**: Each student has different file structure
- **Live Verification**: Must actually navigate to find answers
- **Code Dependencies**: Verification codes tied to actual performance
- **No Answer Sharing**: Different structures = different answers

### Verification Integrity
- **Cryptographic Codes**: Cannot be guessed or generated externally
- **Score Correlation**: Code directly tied to number of correct answers
- **Tamper Detection**: Modified environments create invalid codes
- **Instructor Validation**: Answer keys allow full verification

## 🎓 Educational Benefits

### Practical Skills
- **Real Command Line**: Actual Linux shell experience
- **Problem Solving**: Must figure out how to find information
- **Tool Mastery**: Learn `find`, `grep`, `ls` options
- **File System Understanding**: Navigate complex directory structures

### Assessment Authenticity
- **Performance-Based**: Must demonstrate actual skills
- **No Memorization**: Cannot succeed through rote learning
- **Real-World Applicable**: Skills transfer to system administration
- **Immediate Feedback**: Learn from mistakes during quiz

## 🚨 Troubleshooting

### Common Issues

1. **GUI Won't Start**:
   ```bash
   # Install tkinter
   sudo apt-get install python3-tk
   ```

2. **Shell Commands Fail**:
   ```bash
   # Ensure you're in Linux/WSL environment
   # Check that basic commands work: ls, cd, find
   ```

3. **File Generation Errors**:
   ```bash
   # Check write permissions in current directory
   # Ensure sufficient disk space
   ```

4. **Code Validation Fails**:
   ```bash
   # Verify student ID matches exactly
   # Check assignment key is correct
   # Ensure answer key was generated for this student
   ```

### Testing
```bash
# Run comprehensive test
python test_navigation_quiz.py

# Test answer key generation
python NavigationQuizAnswerKeyGenerator.py
# Choose option 6: Test single student
```

## 📈 Scalability

### Large Classes
- **Batch Processing**: Generate keys for hundreds of students
- **CSV Integration**: Import/export to LMS systems
- **Automated Validation**: Process many codes quickly
- **Performance**: Handles large student lists efficiently

### Customization
- **Question Types**: Easy to add new question categories
- **File Structures**: Modify templates for different complexity
- **Grading Scales**: Adjust number of questions/scoring
- **Time Limits**: Add timing constraints if needed

---

## 🎯 Ready to Deploy!

The Linux Navigation Quiz provides:

✅ **Authentic Assessment**: Students must demonstrate real Linux skills  
✅ **Academic Integrity**: Unique environments prevent cheating  
✅ **Automated Grading**: Verification codes enable instant scoring  
✅ **Educational Value**: Builds practical system administration skills  
✅ **Instructor Friendly**: Easy setup, grading, and LMS integration  

Perfect for testing Linux file system navigation competency in computer science, cybersecurity, and system administration courses!

---

**Happy Teaching & Learning! 🐧📚**
