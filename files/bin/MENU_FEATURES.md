# Linux Tutorial - Menu System

## New Features

### Main Menu System
Students now have the flexibility to choose their learning path:

1. **Complete Tutorial** - All 4 lessons in sequence (35 total exercises)
2. **Individual Lessons** - Choose specific lessons:
   - Lesson 1: Basic Navigation (5 exercises)
   - Lesson 2: File Operations (10 exercises) 
   - Lesson 3: Text Processing (10 exercises)
   - Lesson 4: Permissions (10 exercises)

### Assignment Key Management
- **For Complete Tutorial**: One assignment key covers all lessons
- **For Individual Lessons**: Each lesson requires its own assignment key
- Students are prompted for assignment keys when they start each lesson/tutorial

### Progress Tracking
- **Progress codes** generated every 5 exercises
- **Completion codes** generated when lessons finish
- Each lesson session resets progress tracking
- Students receive codes to submit in Canvas

### Student Workflow
1. Enter student ID and optional name
2. Choose from main menu:
   - `all` - Complete tutorial
   - `1-4` - Specific lesson number
   - `quit` - Exit
3. Enter assignment key for chosen lesson/tutorial
4. Complete exercises and receive progress codes
5. Submit codes in Canvas

### Benefits for Instructors
- Assign specific lessons for targeted learning
- Different assignment keys for different assignments
- Flexible pacing - students can repeat lessons
- Clear progress tracking per lesson
- Easy to manage partial completion

## Usage Example
```bash
python tutorial.py
```

Students will see:
1. Student identification prompt
2. Main menu with lesson choices
3. Assignment key prompt for selected option
4. Lesson content with exercises
5. Progress codes for Canvas submission

## 📚 For Instructors

**See [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md) for complete instructions on:**
- Using the Answer Key Generator (`StudentToGroup.py`)
- Setting up assignments and managing assignment keys
- Generating answer keys for grading validation
- Best practices for course integration
- Troubleshooting common issues
