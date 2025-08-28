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

    def load_lessons(self) -> List[Dict[str, Any]]:
        """Load tutorial lessons configuration"""
        return [
            {
                "title": "Basic Navigation",
                "description": "Learn to navigate the file system",
                "commands": ["pwd", "ls", "ls -l", "ls -a", "ls -la", "cd"],
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
                    }
                ]
            },
            {
                "title": "File Operations",
                "description": "Learn to create, copy, move, and delete files",
                "commands": ["touch", "cp", "mv", "rm"],
                "exercises": [
                    {
                        "instruction": "Create a new file called 'test.txt'",
                        "command": "touch test.txt",
                        "expected_output": None,
                        "verification": "check_file_exists:test.txt"
                    }
                ]
            },
            {
                "title": "Text Processing",
                "description": "Learn to view and process text files",
                "commands": ["cat", "grep", "head", "tail"],
                "exercises": []
            },
            {
                "title": "Permissions",
                "description": "Learn about file permissions and ownership",
                "commands": ["chmod", "chown", "ls -l"],
                "exercises": []
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
        print("🆔 STUDENT IDENTIFICATION")
        print("=" * 40)
        print("Please enter your student information:")
        
        # Get student ID
        while True:
            student_id = input("Student ID (or email): ").strip()
            if student_id:
                self.user_progress['student_id'] = student_id
                break
            print("Please enter a valid student ID.")
        
        # Get assignment key
        print("\n🔑 ASSIGNMENT IDENTIFICATION")
        while True:
            assignment_key = input("Assignment key (provided by instructor): ").strip()
            if assignment_key:
                self.user_progress['assignment_key'] = assignment_key
                break
            print("Please enter the assignment key provided by your instructor.")
        
        # Optional student name
        student_name = input("\nYour name (optional): ").strip()
        if student_name:
            self.user_progress['student_name'] = student_name
        
        # Show session info
        group_number = self.get_student_group(student_id)
        
        print(f"\n✅ Session started for: {student_id}")
        if student_name:
            print(f"   Name: {student_name}")
        print(f"   Assignment: {assignment_key}")
        print(f"   Assigned to Group: {group_number}")
        print(f"   Start time: {self.user_progress['start_time']}")
        print()
    
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
        print("📊 PROGRESS CHECKPOINT REACHED!")
        print("🎯" * 20)
        print(f"Exercises completed: {self.exercise_counter}")
        print(f"Current lesson: {self.current_lesson + 1}/{len(self.lessons)}")
        print(f"Assignment: {self.user_progress['assignment_key']}")
        print()
        print("📝 ENTER THIS CODE IN CANVAS:")
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
        """Start the interactive tutorial"""
        self.setup_student_session()
        self.display_welcome()
        
        # Count total exercises for progress tracking
        self.user_progress['total_exercises'] = sum(len(lesson['exercises']) for lesson in self.lessons)
        
        while self.current_lesson < len(self.lessons):
            lesson = self.lessons[self.current_lesson]
            if self.run_lesson(lesson):
                self.current_lesson += 1
            else:
                break
                
        self.display_completion()
    
    def display_welcome(self):
        """Display welcome message and tutorial overview"""
        print("=" * 60)
        print("🐧 WELCOME TO LINUX COMMAND TUTORIAL 🐧")
        print("=" * 60)
        print()
        print("This interactive tutorial will teach you essential Linux commands.")
        print("You'll learn by doing - each lesson includes hands-on exercises.")
        print()
        print("Available lessons:")
        for i, lesson in enumerate(self.lessons, 1):
            print(f"  {i}. {lesson['title']}: {lesson['description']}")
        print()
        input("Press Enter to begin...")
        print()
    
    def run_lesson(self, lesson: Dict[str, Any]) -> bool:
        """Run a single lesson"""
        print(f"📚 LESSON: {lesson['title']}")
        print("=" * 50)
        print(f"Description: {lesson['description']}")
        print(f"Commands you'll learn: {', '.join(lesson['commands'])}")
        print()
        
        # Show command explanations
        self.explain_commands(lesson['commands'])
        
        # Run exercises
        for i, exercise in enumerate(lesson['exercises'], 1):
            print(f"\n🔧 Exercise {i}:")
            if not self.run_exercise(exercise):
                return False
        
        print(f"\n✅ Lesson '{lesson['title']}' completed!")
        print("=" * 50)
        return True
    
    def explain_commands(self, commands: List[str]):
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
            "chmod": "chmod - Change file permissions",
            "chown": "chown - Change file ownership"
        }
        
        print("📖 Command Reference:")
        for cmd in commands:
            if cmd in explanations:
                print(f"  • {explanations[cmd]}")
        
        # Add special explanation for ls commands
        if any(cmd.startswith('ls') for cmd in commands):
            print("\n📋 Understanding ls -l output:")
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
            
            print("🔍 Common ls options:")
            print("  • ls -l    : Long format (detailed info)")
            print("  • ls -a    : Show hidden files (.filename)")
            print("  • ls -h    : Human readable sizes (KB, MB, GB)")
            print("  • ls -t    : Sort by time (newest first)")
            print("  • ls -r    : Reverse order")
            print("  • ls -S    : Sort by file size")
            print("  • ls -R    : Recursive (show subdirectories)")
            print("  • ls *.txt : List only .txt files (wildcards)")
        print()
    
    def read_student_list(self, filename: str) -> List[str]:
        """Read student list from file (one email per line)"""
        try:
            with open(filename, 'r') as file:
                students = [line.strip() for line in file if line.strip()]
            print(f"✅ Read {len(students)} students from {filename}")
            return students
        except FileNotFoundError:
            print(f"❌ Error: File '{filename}' not found!")
            return []
        except Exception as e:
            print(f"❌ Error reading file: {e}")
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
        
        print(f"📁 Student groups CSV generated: {output_file}")
        print(f"🔧 Used {self.num_groups} groups")
        
        # Print summary
        print("\n📊 GROUP DISTRIBUTION:")
        print("-" * 40)
        for group_name in sorted(groups.keys()):
            count = len(groups[group_name])
            print(f"{group_name}: {count} students")
        print(f"Total: {len(students)} students")
        print("\n✅ Students loaded into memory for answer key generation")

    def generate_answer_keys_for_loaded_students(self, assignment_key: str, max_exercises: int = 20) -> None:
        """Generate answer keys for previously loaded students"""
        if not self.loaded_students:
            print("❌ No students loaded! Use 'load_students' command first.")
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
        
        print(f"📁 Group answer key generated: {group_filename}")
        
        # Generate individual student answer keys
        output_dir = f"individual_keys_{assignment_key}"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"📁 Created directory: {output_dir}")
        
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
        
        print(f"✅ Generated {total_students} individual answer key files in '{output_dir}' directory")
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
            print("❌ No students currently loaded.")
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
                    print(f"✅ Set to {num_groups} groups")
                    # Clear loaded students since group structure changed
                    if self.loaded_students:
                        print("⚠️  Cleared previously loaded students due to group structure change")
                        self.loaded_students = {}
                        self.student_groups = {}
                else:
                    print("❌ Number of groups must be between 2 and 26")
            except ValueError:
                print("❌ Please enter a valid number")
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

    def execute_and_verify(self, user_input: str, exercise: Dict[str, Any]) -> bool:
        """Execute user command and verify it matches the exercise requirements"""
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

    def show_current_progress(self):
        """Display current progress to student"""
        print("\n📈 YOUR PROGRESS")
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
        print("🎉 CONGRATULATIONS! 🎉")
        print("=" * 60)
        print("You have completed the Linux Command Tutorial!")
        print()
        print("📊 FINAL PROGRESS SUMMARY:")
        print(f"  • Student ID: {self.user_progress['student_id']}")
        print(f"  • Assignment: {self.user_progress['assignment_key']}")
        print(f"  • Group: {self.get_student_group(self.user_progress['student_id'])}")
        print(f"  • Total exercises completed: {self.exercise_counter}")
        print(f"  • All {len(self.lessons)} lessons finished")
        print()
        print("🏆 FINAL COMPLETION CODE:")
        print("=" * 40)
        print(f"         {final_code}")
        print("=" * 40)
        print("⚠️  Enter this FINAL code in your LMS to mark completion!")
        print()
        
        # Show all progress codes
        print("📝 All your progress codes:")
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
                print("⏭️  Skipping exercise...")
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
                print("\n----------------------------\n✅ Correct! Well done.")
                
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
                print("❌ That's not quite right. Try again or type 'hint' for help.")
                print("💡 Type 'progress' to see your current progress.")
                print("💡 Type 'admin_help' for administrative commands.")

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
