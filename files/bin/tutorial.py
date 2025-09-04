#!/usr/bin/env python3
"""
Linux Command Tutorial
An interactive tutorial for learning essential Linux commands
"""

import os
import sys
import subprocess
import time
import hashlib
import json
import datetime
import random
from typing import List, Dict, Any

class LinuxTutorial:
    """
    Interactive Linux command tutorial system.
    
    Provides step-by-step lessons on essential Linux commands with
    hands-on practice and verification.
    """
    
    def __init__(self):
        self.current_lesson = 0
        self.user_progress = {
            'student_id': None,
            'assignment_key': None,  # Add assignment key tracking
            'start_time': datetime.datetime.now().isoformat(),
            'completed_exercises': [],
            'completion_codes': [],
            'total_exercises': 0
        }
        self.lessons = self.load_lessons()
        self.progress_checkpoint = 5  # Generate code every 5 exercises
        self.exercise_counter = 0
        self.num_groups = 5  # Default number of groups
        self.loaded_students = {}  # Store students loaded from file
        self.student_groups = {}   # Store student-to-group mapping

    def clear_screen(self):
        """Clear the screen for better readability"""
        # Clear screen - works on Windows, macOS, and Linux
        os.system('cls' if os.name == 'nt' else 'clear')

    def load_lessons(self) -> List[Dict[str, Any]]:
        """Load tutorial lessons configuration"""
        return [
            {
                "title": "Basic Navigation",
                "description": "Learn to navigate the file system and analyze file sizes",
                "commands": ["pwd", "ls", "ls -l", "ls -a", "ls -la", "ls -lh", "cd"],
                "exercises": [
                    {
                        "instruction": "Display your current directory",
                        "command": "pwd",
                        "expected_output": None,
                        "verification": "check_pwd"
                    },
                    {
                        "instruction": "List files in current directory",
                        "command": "ls",
                        "expected_output": None,
                        "verification": "check_ls"
                    },
                    {
                        "instruction": "List files with detailed information (long format)",
                        "command": "ls -l",
                        "expected_output": None,
                        "verification": "check_ls"
                    },
                    {
                        "instruction": "List all files including hidden ones",
                        "command": "ls -a",
                        "expected_output": None,
                        "verification": "check_ls"
                    },
                    {
                        "instruction": "List all files with detailed information",
                        "command": "ls -la",
                        "expected_output": None,
                        "verification": "check_ls"
                    },
                    {
                        "instruction": "List files in the Documents directory with sizes: ls -l Documents",
                        "command": "ls -l Documents",
                        "expected_output": None,
                        "verification": "check_ls"
                    },
                    {
                        "instruction": "Display just the small.txt file information: ls -l Documents/small.txt",
                        "command": "ls -l Documents/small.txt",
                        "expected_output": None,
                        "verification": "check_ls_specific:Documents/small.txt"
                    },
                    {
                        "instruction": "Display just the project.txt file information: ls -l Documents/project.txt",
                        "command": "ls -l Documents/project.txt",
                        "expected_output": None,
                        "verification": "check_ls_specific:Documents/project.txt"
                    },
                    {
                        "instruction": "Compare the sizes of all .txt files: ls -l Documents/*.txt",
                        "command": "ls -l Documents/*.txt",
                        "expected_output": None,
                        "verification": "check_ls"
                    },
                    {
                        "instruction": "Use ls -lh for human-readable file sizes: ls -lh Documents",
                        "command": "ls -lh Documents",
                        "expected_output": None,
                        "verification": "check_ls"
                    }
                ]
            },
            {
                "title": "Document Content Exploration",
                "description": "Learn to read and search through real document files",
                "commands": ["cat", "grep", "head", "tail", "wc"],
                "exercises": [
                    {
                        "instruction": "Read the contents of the smallest file: cat Documents/small.txt",
                        "command": "cat Documents/small.txt",
                        "expected_output": None,
                        "verification": "check_cat_output:Documents/small.txt"
                    },
                    {
                        "instruction": "Read the README file: cat Documents/README.txt",
                        "command": "cat Documents/README.txt",
                        "expected_output": None,
                        "verification": "check_cat_output:Documents/README.txt"
                    },
                    {
                        "instruction": "View the student list: cat Documents/students.txt",
                        "command": "cat Documents/students.txt",
                        "expected_output": None,
                        "verification": "check_cat_output:Documents/students.txt"
                    },
                    {
                        "instruction": "Search for 'Linux' in the README: grep 'Linux' Documents/README.txt",
                        "command": "grep 'Linux' Documents/README.txt",
                        "expected_output": None,
                        "verification": "check_grep_output:Linux:Documents/README.txt"
                    },
                    {
                        "instruction": "Count lines in the project file: wc -l Documents/project.txt",
                        "command": "wc -l Documents/project.txt",
                        "expected_output": None,
                        "verification": "check_command_success"
                    },
                    {
                        "instruction": "Show first 5 lines of project documentation: head -n 5 Documents/project.txt",
                        "command": "head -n 5 Documents/project.txt",
                        "expected_output": None,
                        "verification": "check_head_output:Documents/project.txt"
                    },
                    {
                        "instruction": "Search for 'Computer' in students file: grep 'Computer' Documents/students.txt",
                        "command": "grep 'Computer' Documents/students.txt",
                        "expected_output": None,
                        "verification": "check_grep_output:Computer:Documents/students.txt"
                    },
                    {
                        "instruction": "Count words in the commands reference: wc -w Documents/commands.txt",
                        "command": "wc -w Documents/commands.txt",
                        "expected_output": None,
                        "verification": "check_command_success"
                    },
                    {
                        "instruction": "Show last 3 lines of commands reference: tail -n 3 Documents/commands.txt",
                        "command": "tail -n 3 Documents/commands.txt",
                        "expected_output": None,
                        "verification": "check_tail_output:Documents/commands.txt"
                    },
                    {
                        "instruction": "Count total characters in small.txt: wc -c Documents/small.txt",
                        "command": "wc -c Documents/small.txt",
                        "expected_output": None,
                        "verification": "check_command_success"
                    }
                ]
            },
            {
                "title": "File Operations",
                "description": "Learn to create, copy, move, and delete files",
                "commands": ["touch", "cp", "mv", "rm", "ls -l"],
                "exercises": [
                    {
                        "instruction": "Create a new file called 'test.txt'",
                        "command": "touch test.txt",
                        "expected_output": None,
                        "verification": "check_file_exists:test.txt"
                    },
                    {
                        "instruction": "Use ls -l to see detailed information about the file you just created",
                        "command": "ls -l test.txt",
                        "expected_output": None,
                        "verification": "check_ls_specific:test.txt"
                    },
                    {
                        "instruction": "Create another file called 'sample.txt'",
                        "command": "touch sample.txt",
                        "expected_output": None,
                        "verification": "check_file_exists:sample.txt"
                    },
                    {
                        "instruction": "List all files in the current directory with detailed information",
                        "command": "ls -l",
                        "expected_output": None,
                        "verification": "check_ls"
                    },
                    {
                        "instruction": "Copy 'test.txt' to create a new file called 'test_copy.txt'",
                        "command": "cp test.txt test_copy.txt",
                        "expected_output": None,
                        "verification": "check_file_exists:test_copy.txt"
                    },
                    {
                        "instruction": "Verify the copy was created by listing files",
                        "command": "ls -l",
                        "expected_output": None,
                        "verification": "check_ls"
                    },
                    {
                        "instruction": "Rename 'sample.txt' to 'renamed_sample.txt' using the mv command",
                        "command": "mv sample.txt renamed_sample.txt",
                        "expected_output": None,
                        "verification": "check_file_moved:sample.txt:renamed_sample.txt"
                    },
                    {
                        "instruction": "Confirm the file was renamed by listing the directory",
                        "command": "ls -l",
                        "expected_output": None,
                        "verification": "check_ls"
                    },
                    {
                        "instruction": "Remove the file 'test_copy.txt'",
                        "command": "rm test_copy.txt",
                        "expected_output": None,
                        "verification": "check_file_not_exists:test_copy.txt"
                    },
                    {
                        "instruction": "Verify the file was deleted by listing the directory",
                        "command": "ls -l",
                        "expected_output": None,
                        "verification": "check_ls"
                    }
                ]
            },
            {
                "title": "Text Processing",
                "description": "Learn to view and process text files",
                "commands": ["cat", "grep", "head", "tail", "echo", "wc"],
                "exercises": [
                    {
                        "instruction": "Create a text file with some content using echo command: echo 'Hello Linux World!' > greeting.txt",
                        "command": "echo 'Hello Linux World!' > greeting.txt",
                        "expected_output": None,
                        "verification": "check_file_exists:greeting.txt"
                    },
                    {
                        "instruction": "Display the contents of greeting.txt using cat",
                        "command": "cat greeting.txt",
                        "expected_output": None,
                        "verification": "check_cat_output:greeting.txt"
                    },
                    {
                        "instruction": "Add more content to the file: echo 'This is line 2' >> greeting.txt",
                        "command": "echo 'This is line 2' >> greeting.txt",
                        "expected_output": None,
                        "verification": "check_file_exists:greeting.txt"
                    },
                    {
                        "instruction": "Add another line: echo 'Linux commands are powerful' >> greeting.txt",
                        "command": "echo 'Linux commands are powerful' >> greeting.txt",
                        "expected_output": None,
                        "verification": "check_file_exists:greeting.txt"
                    },
                    {
                        "instruction": "Display the full contents of the file again",
                        "command": "cat greeting.txt",
                        "expected_output": None,
                        "verification": "check_cat_output:greeting.txt"
                    },
                    {
                        "instruction": "Search for the word 'Linux' in the file using grep",
                        "command": "grep 'Linux' greeting.txt",
                        "expected_output": None,
                        "verification": "check_grep_output:Linux:greeting.txt"
                    },
                    {
                        "instruction": "Display only the first 2 lines of the file using head",
                        "command": "head -n 2 greeting.txt",
                        "expected_output": None,
                        "verification": "check_head_output:greeting.txt"
                    },
                    {
                        "instruction": "Display only the last line of the file using tail",
                        "command": "tail -n 1 greeting.txt",
                        "expected_output": None,
                        "verification": "check_tail_output:greeting.txt"
                    },
                    {
                        "instruction": "Count the number of lines in the file using wc -l",
                        "command": "wc -l greeting.txt",
                        "expected_output": None,
                        "verification": "check_command_success"
                    },
                    {
                        "instruction": "Search for all lines containing 'is' (case-insensitive) using grep -i",
                        "command": "grep -i 'is' greeting.txt",
                        "expected_output": None,
                        "verification": "check_grep_output:is:greeting.txt"
                    }
                ]
            },
            {
                "title": "Permissions",
                "description": "Learn about file permissions and ownership",
                "commands": ["chmod", "ls -l", "stat", "mkdir"],
                "exercises": [
                    {
                        "instruction": "Create a script file called 'myscript.sh'",
                        "command": "touch myscript.sh",
                        "expected_output": None,
                        "verification": "check_file_exists:myscript.sh"
                    },
                    {
                        "instruction": "Check the current permissions of myscript.sh using ls -l",
                        "command": "ls -l myscript.sh",
                        "expected_output": None,
                        "verification": "check_ls_specific:myscript.sh"
                    },
                    {
                        "instruction": "Make the script executable for the owner using chmod u+x",
                        "command": "chmod u+x myscript.sh",
                        "expected_output": None,
                        "verification": "check_command_success"
                    },
                    {
                        "instruction": "Verify the permission change by listing the file again",
                        "command": "ls -l myscript.sh",
                        "expected_output": None,
                        "verification": "check_ls_specific:myscript.sh"
                    },
                    {
                        "instruction": "Remove write permission for group and others using chmod go-w",
                        "command": "chmod go-w myscript.sh",
                        "expected_output": None,
                        "verification": "check_command_success"
                    },
                    {
                        "instruction": "Check the permissions again to see the changes",
                        "command": "ls -l myscript.sh",
                        "expected_output": None,
                        "verification": "check_ls_specific:myscript.sh"
                    },
                    {
                        "instruction": "Set specific permissions using numeric notation: chmod 755 myscript.sh",
                        "command": "chmod 755 myscript.sh",
                        "expected_output": None,
                        "verification": "check_command_success"
                    },
                    {
                        "instruction": "Verify the numeric permission setting worked",
                        "command": "ls -l myscript.sh",
                        "expected_output": None,
                        "verification": "check_ls_specific:myscript.sh"
                    },
                    {
                        "instruction": "Create a directory called 'testdir' and check its default permissions",
                        "command": "mkdir testdir",
                        "expected_output": None,
                        "verification": "check_dir_exists:testdir"
                    },
                    {
                        "instruction": "List the directory with permissions to see the default directory permissions",
                        "command": "ls -ld testdir",
                        "expected_output": None,
                        "verification": "check_ls_specific:testdir"
                    }
                ]
            }
        ]
    
    def get_student_group(self, student_id: str) -> int:
        """Assign student to one of N groups based on their student ID"""
        group_hash = hash(student_id) % self.num_groups
        return group_hash + 1  # Groups 1-N instead of 0-(N-1)
        
    def generate_progress_code(self, exercise_count: int) -> str:
        """Generate a 5-character progress code based on student group and assignment key"""
        # Determine which group the student belongs to
        group_number = self.get_student_group(self.user_progress['student_id'])
        
        # Use assignment key from user progress
        assignment_key = self.user_progress['assignment_key'] or "DEFAULT"
        
        # Create a seed based on assignment key, group number and exercise count
        seed_string = f"ASSIGNMENT-{assignment_key}-GROUP{group_number}-{exercise_count}"
        
        # Convert string to numeric seed
        seed_value = hash(seed_string) % (2**32)
        
        # Seed the random number generator
        random.seed(seed_value)
        
        # Generate 5-character alphanumeric code
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        progress_code = ''.join(random.choices(characters, k=5))
        
        return progress_code

    def setup_student_session(self):
        """Set up student identification and session"""
        print("🆔   STUDENT IDENTIFICATION")
        print("=" * 40)
        print("Please enter your student information:")
        
        # Get student ID
        while True:
            student_id = input("Student ID (or email): ").strip()
            if student_id:
                self.user_progress['student_id'] = student_id
                break
            print("Please enter a valid student ID.")
        
        # Optional student name
        student_name = input("\nYour name (optional): ").strip()
        if student_name:
            self.user_progress['student_name'] = student_name
        
        # Show session info
        group_number = self.get_student_group(student_id)
        
        print(f"\n✅  Session started for: {student_id}")
        if student_name:
            print(f"   Name: {student_name}")
        print(f"   Assigned to Group: {group_number}")
        print(f"   Start time: {self.user_progress['start_time']}")
        print()
        print("ℹ️   Note: You'll be asked for assignment keys for each lesson/tutorial.")
    
    def check_progress_checkpoint(self):
        """Check if we've reached a progress checkpoint"""
        if self.exercise_counter > 0 and self.exercise_counter % self.progress_checkpoint == 0:
            self.generate_and_display_code()
    
    def generate_and_display_code(self):
        """Generate and display progress code to student"""
        code = self.generate_progress_code(self.exercise_counter)
        
        # Store the code with metadata
        code_entry = {
            'code': code,
            'exercise_count': self.exercise_counter,
            'assignment_key': self.user_progress['assignment_key'],
            'group_number': self.get_student_group(self.user_progress['student_id']),
            'timestamp': datetime.datetime.now().isoformat(),
            'lesson_progress': f"{self.current_lesson + 1}/{len(self.lessons)}"
        }
        self.user_progress['completion_codes'].append(code_entry)
        
        # Display the code prominently
        print("\n" + "🎯" * 20)
        print("📊  PROGRESS CHECKPOINT REACHED!")
        print("🎯" * 20)
        print(f"Exercises completed: {self.exercise_counter}")
        print(f"Current lesson: {self.current_lesson + 1}/{len(self.lessons)}")
        print(f"Assignment: {self.user_progress['assignment_key']}")
        print()
        print("📝  ENTER THIS CODE IN CANVAS:")
        print("=" * 40)
        print(f"         {code}")
        print("=" * 40)
        print("⚠️  Important: Copy this code and enter it into ")
        print("   the correct assignment in CANVAS to record your progress.")
        print()
        input("Press Enter after you've recorded the code to continue...")
        print("🎯" * 20)
        print()
    
    def start_tutorial(self):
        """Start the interactive tutorial with main menu"""
        self.setup_student_session()
        self.display_welcome()
        
        # Main menu loop
        while True:
            choice = self.display_main_menu()
            
            if choice == 'quit':
                print("\n👋  Thank you for using the Linux Tutorial! Goodbye!")
                break
            elif choice == 'all':
                self.run_all_lessons()
                break
            elif choice.isdigit():
                lesson_index = int(choice) - 1
                if 0 <= lesson_index < len(self.lessons):
                    self.run_single_lesson(lesson_index)
                else:
                    print("❌  Invalid lesson number. Please try again.")
            else:
                print("❌  Invalid choice. Please try again.")

    def display_main_menu(self):
        """Display the main menu and get user choice"""
        print("\n" + "=" * 60)
        print("🎯  LINUX TUTORIAL - MAIN MENU")
        print("=" * 60)
        print("Choose what you'd like to do:")
        print()
        print("📚  Available Lessons:")
        for i, lesson in enumerate(self.lessons, 1):
            exercise_count = len(lesson['exercises'])
            print(f"  {i}. {lesson['title']} ({exercise_count} exercises)")
            print(f"     {lesson['description']}")
        print()
        print("🎯  Options:")
        print("  all  - Complete all lessons in sequence")
        print("  1-4  - Choose a specific lesson number")
        print("  quit - Exit the tutorial")
        print()
        
        while True:
            choice = input("Enter your choice: ").strip().lower()
            if choice in ['quit', 'all'] or choice.isdigit():
                return choice
            print("❌  Please enter 'all', a lesson number (1-4), or 'quit'")

    def run_all_lessons(self):
        """Run all lessons in sequence"""
        # Clear screen for better focus
        self.clear_screen()
        
        print("🚀  Starting complete tutorial...")
        
        # Ask for assignment key once for all lessons
        assignment_key = self.get_assignment_key("Complete Tutorial")
        self.user_progress['assignment_key'] = assignment_key
        
        # Count total exercises for progress tracking
        self.user_progress['total_exercises'] = sum(len(lesson['exercises']) for lesson in self.lessons)
        self.user_progress['completion_codes'] = []  # Reset codes for this session
        
        # Reset counters
        self.current_lesson = 0
        self.exercise_counter = 0
        
        while self.current_lesson < len(self.lessons):
            lesson = self.lessons[self.current_lesson]
            if self.run_lesson(lesson):
                self.current_lesson += 1
            else:
                break
                
        self.display_completion()

    def run_single_lesson(self, lesson_index):
        """Run a single lesson"""
        lesson = self.lessons[lesson_index]
        
        # Clear screen for better focus
        self.clear_screen()
        
        print(f"🎯  Starting lesson: {lesson['title']}")
        
        # Ask for assignment key for this specific lesson
        assignment_key = self.get_assignment_key(lesson['title'])
        self.user_progress['assignment_key'] = assignment_key
        
        # Set up progress tracking for single lesson (reset for this session)
        self.user_progress['total_exercises'] = len(lesson['exercises'])
        self.user_progress['completion_codes'] = []  # Reset codes for this lesson
        self.current_lesson = lesson_index
        self.exercise_counter = 0
        
        if self.run_lesson(lesson):
            self.display_lesson_completion(lesson)
        
        # Ask if they want to continue with another lesson
        print("\n🔄  Would you like to do another lesson?")
        continue_choice = input("Enter 'y' for yes, or anything else to quit: ").strip().lower()
        if continue_choice != 'y':
            print("\n👋  Thank you for using the Linux Tutorial! Goodbye!")

    def get_assignment_key(self, context_name):
        """Get assignment key for a specific lesson or tutorial"""
        print(f"\n🔑  ASSIGNMENT KEY FOR: {context_name}")
        print("=" * 50)
        while True:
            assignment_key = input("Enter the assignment key provided by your instructor: ").strip()
            if assignment_key:
                return assignment_key
            print("❌  Please enter a valid assignment key.")

    def display_lesson_completion(self, lesson):
        """Display completion message for a single lesson"""
        # Generate completion code for this lesson
        final_code = self.generate_progress_code(self.exercise_counter)
        final_code_entry = {
            'code': final_code,
            'exercise_count': self.exercise_counter,
            'assignment_key': self.user_progress['assignment_key'],
            'group_number': self.get_student_group(self.user_progress['student_id']),
            'timestamp': datetime.datetime.now().isoformat(),
            'lesson_progress': f'LESSON_COMPLETED: {lesson["title"]}',
            'type': 'LESSON_COMPLETION'
        }
        self.user_progress['completion_codes'].append(final_code_entry)
        
        print("\n" + "=" * 60)
        print(f"🎉  LESSON COMPLETED: {lesson['title']} 🎉")
        print("=" * 60)
        print(f"✅  You completed {self.exercise_counter} exercises!")
        print()
        print("🏆  LESSON COMPLETION CODE:")
        print("=" * 40)
        print(f"         {final_code}")
        print("=" * 40)
        print("📝  Enter this code in Canvas for this lesson!")
        print()
        
        # Show progress codes if any checkpoints were reached
        if len(self.user_progress['completion_codes']) > 1:
            print("📊  All your progress codes for this lesson:")
            for i, code_entry in enumerate(self.user_progress['completion_codes'], 1):
                if code_entry.get('type') == 'LESSON_COMPLETION':
                    print(f"  {i}. {code_entry['code']} - LESSON COMPLETION")
                else:
                    print(f"  {i}. {code_entry['code']} - CHECKPOINT ({code_entry['exercise_count']} exercises)")
        
        print("=" * 60)
    
    def display_welcome(self):
        """Display welcome message and tutorial overview"""
        print("=" * 60)
        print("🐧  WELCOME TO LINUX COMMAND TUTORIAL  🐧")
        print("=" * 60)
        print()
        print("This interactive tutorial teaches essential Linux commands through")
        print("hands-on exercises. You can choose to:")
        print()
        print("🎯  Complete all lessons in sequence, OR")
        print("🎯  Work on individual lessons as assigned")
        print()
        print("💡  Each lesson or complete tutorial requires its own assignment key")
        print("💡  You'll receive progress codes to submit in Canvas")
        print("💡  Progress codes are generated every 5 exercises")
        print()
    
    def run_lesson(self, lesson: Dict[str, Any]) -> bool:
        """Run a single lesson"""
        # Clear screen for better focus
        self.clear_screen()
        
        print(f"📚  LESSON: {lesson['title']}")
        print("=" * 50)
        print(f"Description: {lesson['description']}")
        print(f"Commands you'll learn: {', '.join(lesson['commands'])}")
        print()
        
        # Show command explanations
        self.explain_commands(lesson['commands'], lesson['title'])
        
        # Run exercises
        for i, exercise in enumerate(lesson['exercises'], 1):
            print(f"\n🔧 Exercise {i}:")
            if not self.run_exercise(exercise):
                return False
        
        print(f"\n✅  Lesson '{lesson['title']}' completed!")
        print("=" * 50)
        return True
    
    def explain_commands(self, commands: List[str], lesson_title: str = ""):
        """Explain what each command does"""
        explanations = {
            "pwd": "pwd - Print Working Directory (shows current location)",
            "ls": "ls - List directory contents (basic view)",
            "ls -l": "ls -l - List files with detailed information (permissions, owner, size, date)",
            "ls -a": "ls -a - List all files including hidden files (starting with .)",
            "ls -la": "ls -la - Combination: all files with detailed information",
            "ls -h": "ls -h - Human readable file sizes (use with -l)",
            "ls -t": "ls -t - Sort by modification time (newest first)",
            "ls -r": "ls -r - Reverse the order of the sort",
            "cd": "cd - Change Directory (navigate to different folders)",
            "touch": "touch - Create empty files or update timestamps",
            "cp": "cp - Copy files or directories",
            "mv": "mv - Move/rename files or directories", 
            "rm": "rm - Remove/delete files or directories",
            "cat": "cat - Display file contents",
            "grep": "grep - Search for patterns in files",
            "head": "head - Display first lines of a file",
            "tail": "tail - Display last lines of a file",
            "echo": "echo - Display text or write text to files",
            "wc": "wc - Word, line, character, and byte count",
            "chmod": "chmod - Change file permissions",
            "chown": "chown - Change file ownership",
            "mkdir": "mkdir - Create directories",
            "stat": "stat - Display detailed file information"
        }
        
        print("📖  Command Reference:")
        for cmd in commands:
            if cmd in explanations:
                print(f"  • {explanations[cmd]}")
        
        # Add special explanation for ls commands (only for Basic Navigation lesson)
        if lesson_title == "Basic Navigation" and any(cmd.startswith('ls') for cmd in commands):
            print("\n📋  Understanding ls -l output:")
            print("  Example: -rw-r--r-- 1 user group 1024 Jan 15 10:30 filename.txt")
            print("           │││││││││ │ │    │     │    │        │")
            print("           │││││││││ │ │    │     │    │        └── filename")
            print("           │││││││││ │ │    │     │    └─────────── date/time")
            print("           │││││││││ │ │    │     └──────────────── size (bytes)")
            print("           │││││││││ └─────────────────────────────── group")
            print("           ││││││││└───────────────────────────────── owner")
            print("           ││││││└──────────────────────────────────── link count")
            print("           └┴┴┴┴┴┴┴┴───────────────────────────────── permissions")
            print("            │ │ │ │")
            print("            │ │ │ └── other permissions (r=read, w=write, x=execute)")
            print("            │ │ └──── group permissions")
            print("            │ └────── owner permissions")
            print("            └──────── file type (- = file, d = directory, l = link)")
            print()
            
            print("🔍  Common ls options:")
            print("  • ls -l    : Long format (detailed info)")
            print("  • ls -a    : Show hidden files (.filename)")
            print("  • ls -h    : Human readable sizes (KB, MB, GB)")
            print("  • ls -t    : Sort by time (newest first)")
            print("  • ls -r    : Reverse order")
            print("  • ls -S    : Sort by file size")
            print("  • ls -R    : Recursive (show subdirectories)")
            print("  • ls *.txt : List only .txt files (wildcards)")
        
        # Add help for echo commands
        if any('echo' in cmd for cmd in commands):
            print("\n📝  Echo command tips:")
            print("  • echo 'text' > file   : Write text to file (overwrites)")
            print("  • echo 'text' >> file  : Append text to file")
            print("  • echo $USER           : Display environment variables")
            print("  • echo 'Hello World'   : Display text to screen")
        
        # Add help for chmod commands
        if any('chmod' in cmd for cmd in commands):
            print("\n🔐  File Permission Basics:")
            print("  • r (read)    = 4")
            print("  • w (write)   = 2") 
            print("  • x (execute) = 1")
            print()
            print("  Permission Examples:")
            print("  • 755 = rwxr-xr-x (owner: rwx, group: r-x, others: r-x)")
            print("  • 644 = rw-r--r-- (owner: rw-, group: r--, others: r--)")
            print("  • 600 = rw------- (owner: rw-, group: ---, others: ---)")
            print()
            print("  Common chmod commands:")
            print("  • chmod u+x file    : Add execute permission for owner")
            print("  • chmod g-w file    : Remove write permission for group")
            print("  • chmod o+r file    : Add read permission for others")
            print("  • chmod 755 file    : Set specific permissions with numbers")
        
        # Add help for text processing commands
        if any(cmd in ['cat', 'grep', 'head', 'tail', 'wc'] for cmd in commands):
            print("\n📄  Text Processing Tips:")
            print("  • cat file.txt        : Display entire file")
            print("  • head -n 5 file.txt  : Show first 5 lines")
            print("  • tail -n 3 file.txt  : Show last 3 lines")
            print("  • grep 'word' file.txt: Search for 'word' in file")
            print("  • grep -i 'word' file : Case-insensitive search")
            print("  • grep -n 'word' file : Show line numbers with matches")
            print("  • wc -l file.txt      : Count lines in file")
            print("  • wc -w file.txt      : Count words in file")
            print("  • wc -c file.txt      : Count characters in file")
        print()
    
    def read_student_list(self, filename: str) -> List[str]:
        """Read student list from file (one email per line)"""
        try:
            with open(filename, 'r') as file:
                students = [line.strip() for line in file if line.strip()]
            print(f"✅  Read {len(students)} students from {filename}")
            return students
        except FileNotFoundError:
            print(f"❌  Error: File '{filename}' not found!")
            return []
        except Exception as e:
            print(f"❌  Error reading file: {e}")
            return []

    def generate_student_groups_from_file(self, student_file: str, output_file: str = "student_groups.csv") -> None:
        """Generate student groups from file and store them in memory"""
        students = self.read_student_list(student_file)
        
        if not students:
            return
        
        # Organize students by group
        groups = {f'Group {chr(65 + i)}': [] for i in range(self.num_groups)}
        student_to_group = {}
        
        for student in students:
            group_num = self.get_student_group(student)
            group_name = f'Group {chr(65 + group_num - 1)}'
            groups[group_name].append(student)
            student_to_group[student] = group_name
        
        # Store in instance variables for later use
        self.loaded_students = groups
        self.student_groups = student_to_group
        
        # Find the maximum number of students in any group (for CSV columns)
        max_students = max(len(group_students) for group_students in groups.values()) if groups else 0
        
        # Write CSV file
        with open(output_file, 'w', newline='') as csvfile:
            import csv
            writer = csv.writer(csvfile)
            
            # Write header row
            header = []
            for group_name in sorted(groups.keys()):
                header.extend([group_name, ''])  # Group name followed by empty column
            writer.writerow(header)
            
            # Write student rows
            for i in range(max_students):
                row = []
                for group_name in sorted(groups.keys()):
                    if i < len(groups[group_name]):
                        row.extend([groups[group_name][i], ''])  # Student email followed by empty column
                    else:
                        row.extend(['', ''])  # Empty cells if no more students in this group
                writer.writerow(row)
        
        print(f"📁  Student groups CSV generated: {output_file}")
        print(f"🔧 Used {self.num_groups} groups")
        
        # Print summary
        print("\n📊  GROUP DISTRIBUTION:")
        print("-" * 40)
        for group_name in sorted(groups.keys()):
            count = len(groups[group_name])
            print(f"{group_name}: {count} students")
        print(f"Total: {len(students)} students")
        print("\n✅  Students loaded into memory for answer key generation")

    def generate_answer_keys_for_loaded_students(self, assignment_key: str, max_exercises: int = 20) -> None:
        """Generate answer keys for previously loaded students"""
        if not self.loaded_students:
            print("❌  No students loaded! Use 'load_students' command first.")
            return
        
        import csv
        import os
        
        checkpoints = list(range(self.progress_checkpoint, max_exercises + 1, self.progress_checkpoint))
        if max_exercises not in checkpoints:
            checkpoints.append(max_exercises)
        
        # Generate group answer key
        group_filename = f"answer_key_{assignment_key}.csv"
        with open(group_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Header with assignment info
            writer.writerow(['Answer Key'])
            writer.writerow(['Assignment Key', assignment_key])
            writer.writerow(['Max Exercises', max_exercises])
            writer.writerow(['Number of Groups', self.num_groups])
            writer.writerow([])  # Empty row
            
            # Progress codes header
            header = ['Group'] + [f'Checkpoint_{cp}' for cp in checkpoints]
            writer.writerow(header)
            
            # Data rows
            for i, group_name in enumerate(sorted(self.loaded_students.keys()), 1):
                if self.loaded_students[group_name]:  # Only include groups that have students
                    row = [group_name]
                    for checkpoint in checkpoints:
                        code = self.generate_progress_code_for_group(i, checkpoint, assignment_key)
                        row.append(code)
                    writer.writerow(row)
        
        print(f"📁  Group answer key generated: {group_filename}")
        
        # Generate individual student answer keys
        output_dir = f"individual_keys_{assignment_key}"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"📁  Created directory: {output_dir}")
        
        total_students = 0
        for group_name, students in self.loaded_students.items():
            if not students:
                continue
                
            group_num = ord(group_name.split()[1]) - 64  # Convert A,B,C back to 1,2,3
            
            for student in students:
                total_students += 1
                # Create filename (sanitize email for filename)
                safe_filename = student.replace('@', '_at_').replace('.', '_')
                filename = os.path.join(output_dir, f"{safe_filename}_answer_key.csv")
                
                with open(filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    
                    # Header with student info
                    writer.writerow(['Student Answer Key'])
                    writer.writerow(['Student ID', student])
                    writer.writerow(['Assigned Group', group_name])
                    writer.writerow(['Group Number', group_num])
                    writer.writerow(['Assignment Key', assignment_key])
                    writer.writerow([])  # Empty row
                    
                    # Progress codes header
                    writer.writerow(['Exercise Count', 'Progress Code', 'Code Type'])
                    
                    # Generate codes for each checkpoint
                    for checkpoint in checkpoints:
                        code = self.generate_progress_code_for_group(group_num, checkpoint, assignment_key)
                        code_type = "FINAL COMPLETION" if checkpoint == max_exercises else "CHECKPOINT"
                        writer.writerow([checkpoint, code, code_type])
        
        print(f"✅  Generated {total_students} individual answer key files in '{output_dir}' directory")
        print(f"🔑 Assignment key used: '{assignment_key}'")

    def generate_progress_code_for_group(self, group_number: int, exercise_count: int, assignment_key: str) -> str:
        """Generate a 5-character progress code for a specific group and assignment"""
        # Create a seed based on assignment key, group number and exercise count
        seed_string = f"ASSIGNMENT-{assignment_key}-GROUP{group_number}-{exercise_count}"
        
        # Convert string to numeric seed
        seed_value = hash(seed_string) % (2**32)
        
        # Seed the random number generator
        random.seed(seed_value)
        
        # Generate 5-character alphanumeric code
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        progress_code = ''.join(random.choices(characters, k=5))
        
        return progress_code

    def show_loaded_students(self):
        """Display currently loaded students"""
        if not self.loaded_students:
            print("❌  No students currently loaded.")
            return
        
        print("\n👥 LOADED STUDENTS:")
        print("=" * 40)
        total = 0
        for group_name in sorted(self.loaded_students.keys()):
            students = self.loaded_students[group_name]
            print(f"\n{group_name} ({len(students)} students):")
            for student in students:
                print(f"  • {student}")
            total += len(students)
        
        print(f"\nTotal: {total} students loaded")
        print("=" * 40)

    def handle_admin_commands(self, command: str) -> bool:
        """Handle administrative commands for instructor use"""
        parts = command.split()
        
        if parts[0] == 'load_students':
            if len(parts) < 2:
                print("Usage: load_students <filename>")
                return True
            
            filename = parts[1]
            self.generate_student_groups_from_file(filename)
            return True
        
        elif parts[0] == 'show_students':
            self.show_loaded_students()
            return True
        
        elif parts[0] == 'generate_keys':
            if len(parts) < 2:
                print("Usage: generate_keys <assignment_key> [max_exercises]")
                return True
            
            assignment_key = parts[1]
            max_exercises = int(parts[2]) if len(parts) > 2 else 20
            self.generate_answer_keys_for_loaded_students(assignment_key, max_exercises)
            return True
        
        elif parts[0] == 'set_groups':
            if len(parts) < 2:
                print("Usage: set_groups <number>")
                return True
            
            try:
                num_groups = int(parts[1])
                if 2 <= num_groups <= 26:
                    self.num_groups = num_groups
                    print(f"✅  Set to {num_groups} groups")
                    # Clear loaded students since group structure changed
                    if self.loaded_students:
                        print("⚠️  Cleared previously loaded students due to group structure change")
                        self.loaded_students = {}
                        self.student_groups = {}
                else:
                    print("❌  Number of groups must be between 2 and 26")
            except ValueError:
                print("❌  Please enter a valid number")
            return True
        
        elif parts[0] == 'admin_help':
            self.show_admin_help()
            return True
        
        return False

    def show_admin_help(self):
        """Show help for administrative commands"""
        print("\n🔧 ADMINISTRATIVE COMMANDS:")
        print("=" * 40)
        print("load_students <file>     - Load students from file and generate groups")
        print("show_students           - Display currently loaded students")
        print("generate_keys <key> [n] - Generate answer keys for loaded students")
        print("set_groups <number>     - Set number of groups (2-26)")
        print("admin_help              - Show this help")
        print("=" * 40)

    def validate_command_input(self, user_input: str) -> tuple[bool, str]:
        """Validate user input to prevent shell hanging issues"""
        # Strip whitespace and check for empty input
        user_input = user_input.strip()
        
        if not user_input:
            return False, "Please enter a command."
        
        # Check for incomplete/problematic commands that might hang
        problematic_patterns = [
            # Shell keywords that expect continuation
            'if', 'then', 'else', 'elif', 'fi', 'case', 'esac', 'while', 'do', 'done', 'for', 'in',
            # Quotes or brackets without closing
            '"', "'", '`', '(', '[', '{',
            # Pipe or redirection without target
            '|', '>', '<', '>>', '<<',
            # Commands that commonly cause issues when incomplete
            'sudo', 'su', 'ssh', 'scp', 'ftp', 'telnet', 'mysql', 'psql',
            # Programming language interpreters
            'python', 'node', 'perl', 'ruby', 'php'
        ]
        
        # Check if input ends with problematic patterns
        for pattern in problematic_patterns:
            if user_input.endswith(pattern) or user_input == pattern:
                return False, f"The command '{user_input}' appears incomplete or might cause issues. Please check your command and try again."
        
        # Check for unclosed quotes
        quote_count = user_input.count('"') + user_input.count("'")
        if quote_count % 2 != 0:
            return False, "You have unclosed quotes in your command. Please close all quotes and try again."
        
        # Check for unmatched brackets/parentheses
        open_brackets = user_input.count('(') + user_input.count('[') + user_input.count('{')
        close_brackets = user_input.count(')') + user_input.count(']') + user_input.count('}')
        if open_brackets != close_brackets:
            return False, "You have unmatched brackets or parentheses. Please check your command and try again."
        
        # Check for standalone incomplete commands
        words = user_input.split()
        if len(words) == 1:
            incomplete_commands = ['as', 'at', 'awk', 'sed', 'find', 'xargs', 'exec']
            if words[0].lower() in incomplete_commands:
                return False, f"The command '{words[0]}' typically requires additional arguments. Please provide a complete command."
        
        return True, ""

    def execute_and_verify(self, user_input: str, exercise: Dict[str, Any]) -> bool:
        """Execute user command and verify it matches the exercise requirements"""
        # First validate the input to prevent shell hanging
        is_valid, error_message = self.validate_command_input(user_input)
        if not is_valid:
            print(f"⚠️  {error_message}")
            print("💡 Tip: Make sure your command is complete and doesn't end with operators like |, >, or unclosed quotes.")
            return False
        
        try:
            # Execute the command
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True, timeout=10)
            
            # Show the command output to the user
            if result.stdout:
                print(result.stdout.strip())
            if result.stderr:
                print(f"Error: {result.stderr.strip()}")
            
            # Verify the command based on the verification method
            verification = exercise.get('verification', '')
            expected_command = exercise.get('command', '')
            
            # Check if the user input matches the expected command (basic check)
            if self.commands_match(user_input, expected_command):
                # Run specific verification if provided
                if verification:
                    return self.run_verification(verification, user_input, result)
                else:
                    # If no specific verification, just check if command succeeded
                    return result.returncode == 0
            else:
                return False
                
        except subprocess.TimeoutExpired:
            print("Command timed out!")
            return False
        except Exception as e:
            print(f"Error executing command: {e}")
            return False

    def commands_match(self, user_input: str, expected: str) -> bool:
        """Check if user input matches expected command (allowing for minor variations)"""
        # Normalize whitespace and compare
        user_normalized = ' '.join(user_input.split())
        expected_normalized = ' '.join(expected.split())
        
        return user_normalized.lower() == expected_normalized.lower()

    def run_verification(self, verification: str, user_input: str, result: subprocess.CompletedProcess) -> bool:
        """Run specific verification checks"""
        if verification == "check_pwd":
            return self.verify_pwd(user_input, result)
        elif verification == "check_ls":
            return self.verify_ls(user_input, result)
        elif verification.startswith("check_file_exists:"):
            filename = verification.split(":", 1)[1]
            return self.verify_file_exists(filename)
        elif verification.startswith("check_file_not_exists:"):
            filename = verification.split(":", 1)[1]
            return self.verify_file_not_exists(filename)
        elif verification.startswith("check_file_moved:"):
            parts = verification.split(":", 2)
            old_filename = parts[1]
            new_filename = parts[2]
            return self.verify_file_moved(old_filename, new_filename)
        elif verification.startswith("check_ls_specific:"):
            filename = verification.split(":", 1)[1]
            return self.verify_ls_specific(filename, user_input, result)
        elif verification.startswith("check_cat_output:"):
            filename = verification.split(":", 1)[1]
            return self.verify_cat_output(filename, user_input, result)
        elif verification.startswith("check_grep_output:"):
            parts = verification.split(":", 2)
            search_term = parts[1]
            filename = parts[2]
            return self.verify_grep_output(search_term, filename, user_input, result)
        elif verification.startswith("check_head_output:"):
            filename = verification.split(":", 1)[1]
            return self.verify_head_output(filename, user_input, result)
        elif verification.startswith("check_tail_output:"):
            filename = verification.split(":", 1)[1]
            return self.verify_tail_output(filename, user_input, result)
        elif verification == "check_command_success":
            return self.verify_command_success(user_input, result)
        elif verification.startswith("check_dir_exists:"):
            dirname = verification.split(":", 1)[1]
            return self.verify_dir_exists(dirname)
        elif verification.startswith("check_files_not_exist:"):
            filenames = verification.split(":", 1)[1]
            return self.verify_files_not_exist(filenames)
        else:
            # Default: command succeeded
            return result.returncode == 0

    def verify_pwd(self, user_input: str, result: subprocess.CompletedProcess) -> bool:
        """Verify pwd command execution"""
        # Check if command succeeded and produced output
        if result.returncode == 0 and result.stdout.strip():
            # pwd should output a directory path
            output = result.stdout.strip()
            if output.startswith('/') or (os.name == 'nt' and ':' in output):
                return True
        return False

    def verify_ls(self, user_input: str, result: subprocess.CompletedProcess) -> bool:
        """Verify ls command execution"""
        # ls command should succeed (return code 0)
        # Output can be empty (empty directory) or contain files/directories
        return result.returncode == 0

    def verify_file_exists(self, filename: str) -> bool:
        """Verify that a file exists"""
        return os.path.exists(filename)

    def verify_file_not_exists(self, filename: str) -> bool:
        """Verify that a file does not exist"""
        return not os.path.exists(filename)

    def verify_file_moved(self, old_filename: str, new_filename: str) -> bool:
        """Verify that a file was moved (old file gone, new file exists)"""
        return not os.path.exists(old_filename) and os.path.exists(new_filename)

    def verify_ls_specific(self, filename: str, user_input: str, result: subprocess.CompletedProcess) -> bool:
        """Verify ls command for a specific file"""
        if result.returncode == 0:
            # Check if the filename appears in the output
            return filename in result.stdout
        return False

    def verify_cat_output(self, filename: str, user_input: str, result: subprocess.CompletedProcess) -> bool:
        """Verify cat command produces output"""
        return result.returncode == 0 and len(result.stdout.strip()) > 0

    def verify_grep_output(self, search_term: str, filename: str, user_input: str, result: subprocess.CompletedProcess) -> bool:
        """Verify grep command finds the search term"""
        if result.returncode == 0:
            # Check if the search term appears in output (case-insensitive if -i flag used)
            if '-i' in user_input.lower():
                return search_term.lower() in result.stdout.lower()
            else:
                return search_term in result.stdout
        return False

    def verify_head_output(self, filename: str, user_input: str, result: subprocess.CompletedProcess) -> bool:
        """Verify head command produces output"""
        return result.returncode == 0 and len(result.stdout.strip()) > 0

    def verify_tail_output(self, filename: str, user_input: str, result: subprocess.CompletedProcess) -> bool:
        """Verify tail command produces output"""
        return result.returncode == 0 and len(result.stdout.strip()) > 0

    def verify_command_success(self, user_input: str, result: subprocess.CompletedProcess) -> bool:
        """Verify command executed successfully (return code 0)"""
        return result.returncode == 0

    def verify_dir_exists(self, dirname: str) -> bool:
        """Verify that a directory exists"""
        return os.path.exists(dirname) and os.path.isdir(dirname)

    def verify_files_not_exist(self, filenames: str) -> bool:
        """Verify that multiple files do not exist (comma-separated list)"""
        files = [f.strip() for f in filenames.split(',')]
        for filename in files:
            if os.path.exists(filename):
                return False
        return True

    def show_current_progress(self):
        """Display current progress to student"""
        print("\n📈  YOUR PROGRESS")
        print("=" * 30)
        print(f"Student ID: {self.user_progress.get('student_id', 'Not set')}")
        print(f"Assignment: {self.user_progress.get('assignment_key', 'Not set')}")
        if self.user_progress.get('student_id'):
            print(f"Group: {self.get_student_group(self.user_progress['student_id'])}")
        print(f"Exercises completed: {self.exercise_counter}/{self.user_progress['total_exercises']}")
        print(f"Current lesson: {self.current_lesson + 1}/{len(self.lessons)}")
        print(f"Progress codes generated: {len(self.user_progress['completion_codes'])}")
        
        if self.user_progress['completion_codes']:
            print("\n🎯 Your progress codes:")
            for code_entry in self.user_progress['completion_codes']:
                print(f"  • {code_entry['code']} (after {code_entry['exercise_count']} exercises)")
        
        print("=" * 30)
        print()

    def display_completion(self):
        """Display tutorial completion message with final code"""
        # Generate final completion code
        final_code = self.generate_progress_code(self.exercise_counter)
        final_code_entry = {
            'code': final_code,
            'exercise_count': self.exercise_counter,
            'assignment_key': self.user_progress['assignment_key'],
            'group_number': self.get_student_group(self.user_progress['student_id']),
            'timestamp': datetime.datetime.now().isoformat(),
            'lesson_progress': 'COMPLETED',
            'type': 'FINAL_COMPLETION'
        }
        self.user_progress['completion_codes'].append(final_code_entry)
        
        print("\n" + "=" * 60)
        print("🎉  CONGRATULATIONS! 🎉")
        print("=" * 60)
        print("You have completed the Linux Command Tutorial!")
        print()
        print("📊  FINAL PROGRESS SUMMARY:")
        print(f"  • Student ID: {self.user_progress['student_id']}")
        print(f"  • Assignment: {self.user_progress['assignment_key']}")
        print(f"  • Group: {self.get_student_group(self.user_progress['student_id'])}")
        print(f"  • Total exercises completed: {self.exercise_counter}")
        print(f"  • All {len(self.lessons)} lessons finished")
        print()
        print("🏆  FINAL COMPLETION CODE:")
        print("=" * 40)
        print(f"         {final_code}")
        print("=" * 40)
        print("⚠️   Enter this FINAL code in your LMS to mark completion!")
        print()
        
        # Show all progress codes
        print("📝  All your progress codes:")
        for i, code_entry in enumerate(self.user_progress['completion_codes'], 1):
            code_type = "CHECKPOINT" if code_entry.get('type') != 'FINAL_COMPLETION' else "FINAL"
            print(f"  {i}. {code_entry['code']} - {code_type} ({code_entry['exercise_count']} exercises)")
        
        print("\n" + "=" * 60)

    def calculate_session_duration(self):
        """Calculate how long the session has been running"""
        start_time = datetime.datetime.fromisoformat(self.user_progress['start_time'])
        duration = datetime.datetime.now() - start_time
        
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60
        
        if hours > 0:
            return f"{hours}h {minutes}m"
        else:
            return f"{minutes}m"
    
    def run_exercise(self, exercise: Dict[str, Any]) -> bool:
        """Run a single exercise"""
        print(f"Task: {exercise['instruction']}")
        print(f"Command to try: {exercise['command']}")
        print()
        
        while True:
            user_input = input("$ ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                return False
            elif user_input.lower() in ['help', 'hint']:
                print(f"Hint: Try typing '{exercise['command']}'")
                continue
            elif user_input.lower() == 'skip':
                print("⏭️   Skipping exercise...")
                return True
            elif user_input.lower() == 'progress':
                self.show_current_progress()
                continue
            elif user_input.startswith('admin:') or user_input in ['load_students', 'show_students', 'generate_keys', 'set_groups', 'admin_help']:
                # Handle admin commands
                admin_command = user_input.replace('admin:', '') if user_input.startswith('admin:') else user_input
                if self.handle_admin_commands(admin_command):
                    continue
        
        # Execute the command and verify (MOVE THIS INSIDE THE WHILE LOOP)

            if self.execute_and_verify(user_input, exercise):
                print("\n----------------------------\n✅  Correct! Well done.")
                
                # Track exercise completion
                self.exercise_counter += 1
                exercise_record = {
                    'exercise': exercise['instruction'],
                    'command': exercise['command'],
                    'user_input': user_input,
                    'timestamp': datetime.datetime.now().isoformat()
                }
                self.user_progress['completed_exercises'].append(exercise_record)
                
                # Check for progress checkpoint
                self.check_progress_checkpoint()
                
                # Pause before continuing to next exercise
                print()
                input("Press Enter to continue to the next exercise...")
                print()
                
                return True
            else:
                print("❌  That's not quite right. Try again or type 'hint' for help.")
                print("💡  Type 'progress' to see your current progress.")
                print("💡  Type 'admin_help' for administrative commands.")

def main():
    """Main entry point"""
    try:
        tutorial = LinuxTutorial()
        tutorial.start_tutorial()
    except KeyboardInterrupt:
        print("\n\nTutorial interrupted. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
