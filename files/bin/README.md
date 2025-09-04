# Linux Command Tutorial System

A comprehensive interactive tutorial system for teaching essential Linux commands with automated progress tracking and grading support.

## 📚 System Overview

This tutorial system consists of:

- **`tutorial.py`** - Interactive student tutorial with menu-driven lessons
- **`StudentToGroup.py`** - Answer key generator for instructor grading
- **Documentation** - Comprehensive guides for students and instructors

## 🎯 Features

### For Students
- **Interactive lessons** with hands-on Linux command practice
- **Flexible learning paths** - individual lessons or complete tutorial
- **Automated progress tracking** with validation codes
- **Real-time feedback** on command execution
- **Comprehensive help** with command explanations

### For Instructors
- **Automated answer key generation** for any assignment
- **Flexible assignment management** with unique assignment keys
- **Student group management** with hash-based assignment
- **LMS integration** ready with CSV exports
- **Validation tools** for grading student submissions

## 📖 Quick Start

### Students
```bash
python tutorial.py
```
Follow the prompts to:
1. Enter your student ID/email
2. Choose a lesson or complete tutorial
3. Enter the assignment key provided by instructor
4. Complete exercises and submit progress codes

### Instructors
```bash
python StudentToGroup.py
```
Use the interactive menu to:
1. Set assignment keys
2. Generate answer keys from student lists
3. Validate student submissions

## 📋 Tutorial Content

The tutorial includes a comprehensive `Documents/` directory with sample files of various sizes and types for realistic practice:

| Lesson | Title | Exercises | Commands | Practice Focus |
|--------|-------|-----------|----------|----------------|
| 1 | Basic Navigation | 10 | `pwd`, `ls`, `ls -l`, `ls -lh`, `cd` | Navigate, explore files, analyze file sizes |
| 2 | Document Content Exploration | 10 | `cat`, `grep`, `head`, `tail`, `wc` | Read content, search documents, count data |
| 3 | File Operations | 10 | `touch`, `cp`, `mv`, `rm`, `ls -l` | Create, copy, move, delete files |
| 4 | Text Processing | 10 | `cat`, `grep`, `head`, `tail`, `echo`, `wc` | Text creation and manipulation |
| 5 | Permissions | 10 | `chmod`, `mkdir`, `ls -l` | File permissions and ownership |

**Total: 50 exercises** across all lessons

### Sample Files Included
- **`small.txt`** (12 bytes) - Simple "Hello World" content
- **`README.txt`** (205 bytes) - Tutorial welcome message  
- **`students.txt`** (163 bytes) - Sample student roster
- **`commands.txt`** (331 bytes) - Linux command reference
- **`medium.txt`** (519 bytes) - Multi-paragraph educational content
- **`project.txt`** (1,775 bytes) - Comprehensive project documentation
- **`script.sh`** (108 bytes) - Example shell script for permissions practice

Students explore these real files, learning to:
- **Compare file sizes** using `ls -l` and `ls -lh` output
- **Read and search file content** with `cat` and `grep`
- **Analyze file permissions** and modify script executability
- **Navigate directory structures** and understand file organization

## 📚 Documentation

### For Instructors
- **[INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md)** - Complete instructor manual
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick reference card
- **[instructor_demo.py](instructor_demo.py)** - Working example

### For Students/System Info
- **[MENU_FEATURES.md](MENU_FEATURES.md)** - Menu system overview

## 🚀 Example Usage

### Instructor Workflow
```bash
# 1. Generate answer key
python StudentToGroup.py
# Choose: Set assignment key → Generate master answer key

# 2. Give students the assignment key and instructions
# 3. Students complete tutorial and submit codes
# 4. Validate submissions against generated answer key
```

### Student Workflow
```bash
# 1. Start tutorial
python tutorial.py

# 2. Enter student information
Student ID: john.doe@university.edu
Assignment Key: BasicNav_Week3

# 3. Choose lesson or complete tutorial
# 4. Complete exercises
# 5. Submit progress codes to LMS
```

## 🔧 System Requirements

- **Python 3.6+**
- **Standard libraries only** (no additional installations)
- **Cross-platform** (Windows, macOS, Linux)

## 🎯 Assignment Strategies

### Weekly Individual Lessons
- Week 3: Basic Navigation (10 exercises)
- Week 5: Document Content Exploration (10 exercises)  
- Week 7: File Operations (10 exercises)
- Week 9: Text Processing (10 exercises)
- Week 11: Permissions (10 exercises)

### Comprehensive Assessments
- Midterm: First three lessons (30 exercises)
- Final: Complete tutorial (50 exercises)

## 🔒 Security Features

- **Hash-based student grouping** prevents code sharing
- **Assignment key isolation** ensures unique codes per assignment
- **Deterministic code generation** for reliable validation
- **No student data persistence** for privacy

## 📊 Progress Tracking

- **Checkpoint codes** generated every 5 exercises
- **Completion codes** when lessons/tutorial finish
- **CSV export format** for LMS integration
- **Individual and group answer keys** available

## 🆘 Support

### Common Issues
- **Codes don't match**: Verify assignment key and student ID format
- **Missing progress**: Check if student reached checkpoint (every 5 exercises)
- **System compatibility**: Both programs use identical algorithms

### Testing
- Run `instructor_demo.py` for a complete workflow example
- Use "Test single student ID" option in StudentToGroup.py
- Create sample student files for testing

## 📁 File Structure

```
LinuxTutorial/
├── tutorial.py              # Main student tutorial
├── StudentToGroup.py        # Answer key generator
├── instructor_demo.py       # Working example for instructors
├── Documents/               # Sample files for practice
│   ├── README.txt          # Tutorial introduction (205 bytes)
│   ├── small.txt           # Tiny file for size comparison (12 bytes)
│   ├── students.txt        # Sample student list (163 bytes)
│   ├── commands.txt        # Linux command reference (331 bytes)
│   ├── medium.txt          # Multi-line content (519 bytes)
│   ├── project.txt         # Large documentation file (1,775 bytes)
│   └── script.sh           # Example shell script (108 bytes)
├── INSTRUCTOR_GUIDE.md      # Complete instructor manual
├── QUICK_REFERENCE.md       # Quick reference card
├── MENU_FEATURES.md         # System overview
└── README.md               # This file
```

## 🏆 Benefits

### Educational
- **Hands-on learning** with real command execution
- **Progressive difficulty** from basic to advanced concepts
- **Immediate feedback** and error correction
- **Comprehensive command coverage** for Linux basics

### Administrative  
- **Automated grading** with validation codes
- **Flexible assignment structure** for different course needs
- **Easy LMS integration** with CSV exports
- **Scalable** for large classes

---

**Ready to get started? See [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md) for detailed setup instructions.**
