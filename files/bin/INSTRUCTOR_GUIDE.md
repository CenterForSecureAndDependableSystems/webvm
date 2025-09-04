# Linux Tutorial - In| 3 | Text Processing | 10 | `cat`, `grep`, `head`, `tail`, `echo`, `wc` |
| 4 | Permissions | 10 | `chmod`, `mkdir`, permission management |

**Total: 35 exercises** when completing all lessonsctor Guide

## Overview

This Linux Tutorial system provides an interactive learning environment for students to practice essential Linux commands. The system includes:

- **Student Tutorial Program** (`tutorial.py`) - Interactive lessons for students
- **Answer Key Generator** (`StudentToGroup.py`) - Tools for instructors to generate grading keys
- **Menu-driven interface** - Flexible lesson selection
- **Progress tracking** - Automated code generation for LMS integration

---

## 📚 Lesson Structure

The tutorial contains 4 comprehensive lessons:

| Lesson | Title | Exercises | Commands Covered |
|--------|-------|-----------|------------------|
| 1 | Basic Navigation | 5 | `pwd`, `ls`, `cd` (various options) |
| 2 | File Operations | 10 | `touch`, `cp`, `mv`, `rm`, `ls -l` |
| 3 | Text Processing | 8 | `cat`, `grep`, `head`, `tail`, `echo` |
| 4 | Permissions | 8 | `chmod`, `ls -l`, permission management |

**Total: 31 exercises** when completing all lessons

---

## 🎯 Assignment Options for Students

### Option 1: Complete Tutorial
- Students select "all" from main menu
- One assignment key covers all 4 lessons (35 exercises)
- Progress codes generated every 5 exercises
- Final completion code after all exercises

### Option 2: Individual Lessons
- Students select specific lesson numbers (1-4)
- Each lesson requires its own assignment key
- Progress codes generated every 5 exercises within that lesson
- Completion code when lesson finishes

---

## 🔑 Answer Key Generator Usage

The `StudentToGroup.py` program helps instructors generate answer keys for validation and grading.

### Getting Started

1. **Run the Answer Key Generator:**
   ```bash
   python StudentToGroup.py
   ```

2. **You'll see the interactive menu:**
   ```
   🖥️  INTERACTIVE GROUP HASH GENERATOR
   Choose an option:
   1. Set assignment key
   2. Generate student groups from file (hash-based)
   3. Load existing student groups from CSV file
   4. Generate answer key CSV (by groups)
   5. Generate individual answer keys (separate files)
   6. Generate master answer key (all students in one file)
   7. Generate answer keys from loaded groups
   8. Test single student ID
   9. Create sample student file
   10. Exit
   ```

### Step-by-Step Workflow

#### Step 1: Set Assignment Key
- Choose option **1**
- Enter a unique assignment key (e.g., "BasicNav_Week3", "FileOps_Midterm", "CompleteReview_Final")
- This key will be used to generate unique progress codes

#### Step 2: Prepare Student List
- Create a text file with student emails/IDs (one per line)
- Example `students.txt`:
  ```
  john.doe@university.edu
  jane.smith@university.edu
  alice.johnson@university.edu
  ```
- Or use option **9** to create a sample file for testing

#### Step 3: Generate Answer Keys

##### Option A: Master Answer Key (Recommended)
- Choose option **6**
- Enter your student list filename
- Enter max exercises (5 for individual lessons, 31 for complete tutorial)
- Enter output filename (e.g., `BasicNav_Week3_answers.csv`)

**Result:** Single CSV file with all students and their expected progress codes

##### Option B: Individual Answer Keys
- Choose option **5** 
- Creates separate CSV file for each student
- Useful for personalized feedback or individual grade tracking

##### Option C: Group-Based Answer Key
- Choose option **4**
- Creates answer key organized by groups (A-E)
- Shows codes for each group rather than individual students

### Example Usage Scenarios

#### Scenario 1: Basic Navigation Lesson
```
Assignment Key: BasicNav_Week3
Max Exercises: 5
Expected Student Codes: After 5 exercises (lesson completion)
```

#### Scenario 2: File Operations Lesson  
```
Assignment Key: FileOps_Week5
Max Exercises: 10
Expected Student Codes: After 5 exercises (checkpoint) and 10 exercises (completion)
```

#### Scenario 3: Complete Tutorial
```
Assignment Key: CompleteLinux_Final
Max Exercises: 35
Expected Student Codes: After 5, 10, 15, 20, 25, 30, 35 exercises
```

---

## 📊 Understanding the Answer Key Output

### Master Answer Key CSV Format
```csv
Master Answer Key
Assignment Key,BasicNav_Week3
Max Exercises,5

Student ID,Group,Checkpoint_5
john.doe@university.edu,Group B,9GEKX
jane.smith@university.edu,Group C,QS9OW
alice.johnson@university.edu,Group E,XKOXY
```

### Key Components:
- **Student ID**: Email or ID used by student
- **Group**: Automatically assigned group (A-E) based on student ID hash
- **Checkpoint Codes**: Expected progress codes for validation

---

## ✅ Validating Student Submissions

### In Canvas/LMS:
1. Students submit their progress codes
2. Compare submitted codes with your answer key
3. Codes must match exactly for credit
4. Different assignment keys produce different codes (prevents sharing)

### Validation Process:
1. **Locate student** in your answer key CSV
2. **Check their group assignment** 
3. **Compare submitted code** with expected code for that exercise count
4. **Award credit** if codes match exactly

---

## 🔍 Troubleshooting & Testing

### Test Single Student ID (Option 8)
- Use this to check what group and codes a specific student should get
- Helpful for debugging or answering student questions

### Verify System Compatibility
- Both `tutorial.py` and `StudentToGroup.py` use the same algorithm
- Same student ID + assignment key + exercise count = same code
- Students cannot guess or share codes between assignments

---

## 📋 Best Practices for Instructors

### Assignment Key Management
- **Use descriptive keys**: `BasicNav_Week3` not `Assignment1`
- **Include semester/year**: `FileOps_Fall2024` for future reference
- **Keep keys unique**: Different assignments need different keys
- **Document keys**: Keep a record of which keys are used for what

### Student Management
- **Consistent student IDs**: Students should use the same email/ID format
- **Export student lists**: Get student emails from your LMS
- **Test with sample**: Use option 9 to create test data first

### Grade Book Integration
- **Import CSV data** into Excel/Google Sheets for grade calculations
- **Sort by group** to see patterns in student performance
- **Track progress codes** to identify when students completed work

### Common Assignment Scenarios

#### Weekly Individual Lessons
```bash
# Week 3: Basic Navigation
Assignment Key: BasicNav_Week3
Max Exercises: 5

# Week 5: File Operations  
Assignment Key: FileOps_Week5
Max Exercises: 10

# Week 7: Text Processing
Assignment Key: TextProc_Week7
Max Exercises: 10

# Week 9: Permissions
Assignment Key: Perms_Week9
Max Exercises: 10
```

#### Comprehensive Assessments
```bash
# Midterm: First two lessons
Assignment Key: Midterm_Nav_Files
Student Instructions: Complete lessons 1-2 with this key

# Final: Complete tutorial
Assignment Key: Final_AllLessons
Student Instructions: Complete all lessons with this key
```

---

## 🎯 Student Instructions Template

**For Individual Lessons:**
```
1. Run: python tutorial.py
2. Enter your university email as Student ID
3. Choose lesson number: [1-4]
4. Enter assignment key: [YourAssignmentKey]
5. Complete all exercises
6. Submit your completion code in Canvas
```

**For Complete Tutorial:**
```
1. Run: python tutorial.py
2. Enter your university email as Student ID  
3. Choose: all
4. Enter assignment key: [YourAssignmentKey]
5. Complete all 35 exercises across 4 lessons
6. Submit progress codes as they appear (every 5 exercises)
7. Submit final completion code in Canvas
```

---

## 🔧 Advanced Features

### Loading Existing Student Groups
- If you have pre-assigned student groups in CSV format
- Use option **3** to load existing group assignments
- Then use option **7** to generate keys from loaded groups

### Batch Processing
- Generate keys for multiple assignments at once
- Use command-line scripts to automate answer key generation
- Export data in formats compatible with your LMS

---

## 📞 Support & Questions

### Common Issues:
- **Student codes don't match**: Verify they used correct assignment key and student ID
- **Missing progress codes**: Students may not have reached checkpoint (every 5 exercises)
- **Different codes for same student**: Check if assignment keys match exactly

### System Requirements:
- Python 3.6+ 
- Standard libraries only (no additional installations needed)
- Works on Windows, Mac, Linux

For technical questions or issues, verify that both `tutorial.py` and `StudentToGroup.py` are using the same algorithm by running the compatibility tests provided.
