#!/usr/bin/env python3
"""
Linux Navigation Quiz
Interactive quiz with live shell and auto-generated file structure
"""

import os
import sys
import subprocess
import hashlib
import random
import json
import datetime
import time
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from typing import Dict, List, Any, Tuple

class LinuxNavigationQuiz:
    """
    Interactive Linux navigation quiz with dual-window interface
    """
    
    def __init__(self):
        self.student_id = None
        self.assignment_key = None
        self.quiz_data = {}
        self.questions = []
        self.current_question = 0
        self.answers = {}
        self.score = 0
        self.quiz_directory = "QuizEnvironment"
        
        # GUI components
        self.root = None
        self.instruction_frame = None
        self.shell_frame = None
        self.question_label = None
        self.answer_entry = None
        self.submit_button = None
        self.shell_text = None
        self.shell_entry = None
        self.progress_label = None
        
        # Shell process
        self.shell_process = None
        self.shell_running = False
        
    def setup_student_session(self):
        """Setup student information and assignment key"""
        print("🧭 Linux Navigation Quiz Setup")
        print("=" * 40)
        
        self.student_id = input("Enter your student ID or email: ").strip()
        if not self.student_id:
            print("❌ Student ID is required")
            return False
            
        self.assignment_key = input("Enter assignment key provided by instructor: ").strip()
        if not self.assignment_key:
            print("❌ Assignment key is required")
            return False
            
        print(f"✅ Student: {self.student_id}")
        print(f"✅ Assignment: {self.assignment_key}")
        return True
        
    def generate_file_structure(self):
        """Generate unique file structure based on student ID and assignment key"""
        # Create deterministic random seed from student info
        seed_string = f"{self.student_id}:{self.assignment_key}"
        seed = int(hashlib.md5(seed_string.encode()).hexdigest()[:8], 16)
        random.seed(seed)
        
        # Clean up any existing quiz directory
        if os.path.exists(self.quiz_directory):
            subprocess.run(f'rm -rf "{self.quiz_directory}"', shell=True, cwd=os.getcwd())
        
        # Create main quiz directory
        os.makedirs(self.quiz_directory, exist_ok=True)
        
        # Generate directory structure
        directories = [
            "documents", "projects", "backup", "config", "temp",
            "documents/reports", "documents/drafts", "projects/web",
            "projects/mobile", "backup/weekly", "backup/daily"
        ]
        
        for directory in directories:
            dir_path = os.path.join(self.quiz_directory, directory)
            os.makedirs(dir_path, exist_ok=True)
            
        # Generate files with specific attributes
        self.quiz_data = {
            'files': [],
            'directories': directories,
            'hidden_files': [],
            'large_files': [],
            'specific_content': {}
        }
        
        # File templates with random content
        file_templates = [
            ("readme.txt", "documents", "This is a README file with instructions for the project."),
            ("config.conf", "config", "server_port=8080\ndatabase_host=localhost\ndebug=true"),
            ("report.doc", "documents/reports", "Annual Sales Report\nQ4 Performance: Excellent\nTotal Revenue: $2.5M"),
            ("backup.tar", "backup/weekly", "Binary backup file content - compressed data"),
            ("index.html", "projects/web", "<html><head><title>My Website</title></head><body>Hello World</body></html>"),
            ("app.py", "projects/mobile", "#!/usr/bin/env python3\ndef main():\n    print('Mobile App')\nif __name__ == '__main__':\n    main()"),
            ("data.csv", "documents", "Name,Age,City\nJohn,25,Portland\nJane,30,Seattle\nBob,35,Denver"),
            ("notes.txt", "temp", "Meeting notes from today:\n- Review project timeline\n- Update documentation"),
            (".hidden_config", "config", "SECRET_KEY=abc123xyz789\nAPI_TOKEN=hidden_value"),
            (".profile", ".", "export PATH=$PATH:/usr/local/bin\nalias ll='ls -la'"),
        ]
        
        # Generate files with student-specific modifications
        for base_name, directory, base_content in file_templates:
            # Modify filename slightly based on student
            name_modifier = random.randint(1, 99)
            if '.' in base_name:
                name, ext = base_name.rsplit('.', 1)
                filename = f"{name}{name_modifier}.{ext}"
            else:
                filename = f"{base_name}{name_modifier}"
                
            # Modify content
            student_modifier = f"Student: {self.student_id[:8]}"
            content = f"{base_content}\n\n# {student_modifier}\n# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
            
            # Create file
            if directory == ".":
                file_path = os.path.join(self.quiz_directory, filename)
            else:
                file_path = os.path.join(self.quiz_directory, directory, filename)
                
            with open(file_path, 'w') as f:
                f.write(content)
                
            # Track file info
            file_info = {
                'name': filename,
                'path': file_path,
                'directory': directory,
                'size': len(content.encode()),
                'content': content,
                'is_hidden': filename.startswith('.')
            }
            
            self.quiz_data['files'].append(file_info)
            
            if filename.startswith('.'):
                self.quiz_data['hidden_files'].append(file_info)
                
            if len(content) > 200:
                self.quiz_data['large_files'].append(file_info)
                
        # Add some specific content files for targeted questions
        specific_files = [
            ("secret_code.txt", "temp", f"SECRET_CODE_{random.randint(10000, 99999)}"),
            ("student_info.dat", "documents", f"Student ID: {self.student_id}\nQuiz Date: {datetime.datetime.now().strftime('%Y-%m-%d')}"),
            ("size_test.log", "backup/daily", "X" * random.randint(500, 1500))  # Variable size file
        ]
        
        for filename, directory, content in specific_files:
            file_path = os.path.join(self.quiz_directory, directory, filename)
            with open(file_path, 'w') as f:
                f.write(content)
                
            self.quiz_data['specific_content'][filename] = {
                'path': file_path,
                'content': content,
                'size': len(content.encode())
            }
            
        print(f"✅ Generated file structure in {self.quiz_directory}/")
        print(f"📁 {len(directories)} directories, {len(self.quiz_data['files']) + len(specific_files)} files")
        
    def generate_questions(self):
        """Generate quiz questions based on the created file structure"""
        self.questions = []
        
        # Question 1: Find a specific file
        target_file = random.choice(self.quiz_data['files'])
        self.questions.append({
            'question': f"What is the full path (relative to QuizEnvironment/) of the file named '{target_file['name']}'?",
            'answer': os.path.relpath(target_file['path'], self.quiz_directory).replace('\\', '/'),
            'type': 'path',
            'hint': f"Look in the {target_file['directory']} directory"
        })
        
        # Question 2: Count files in a directory
        target_dir = random.choice(['documents', 'projects', 'config'])
        dir_files = [f for f in self.quiz_data['files'] if f['directory'].startswith(target_dir)]
        self.questions.append({
            'question': f"How many files (not including subdirectories) are in the '{target_dir}' directory? (Include hidden files)",
            'answer': str(len(dir_files)),
            'type': 'count',
            'hint': f"Use 'ls -la' to see hidden files too"
        })
        
        # Question 3: File size
        size_file = list(self.quiz_data['specific_content'].values())[2]  # size_test.log
        self.questions.append({
            'question': f"What is the size in bytes of the file 'size_test.log' in backup/daily/?",
            'answer': str(size_file['size']),
            'type': 'size',
            'hint': "Use 'ls -l' to see file sizes in bytes"
        })
        
        # Question 4: Hidden files
        hidden_count = len([f for f in self.quiz_data['files'] if f['is_hidden']])
        self.questions.append({
            'question': f"How many hidden files (starting with .) are in the entire QuizEnvironment directory tree?",
            'answer': str(hidden_count + 1),  # +1 for .profile in root
            'type': 'count',
            'hint': "Use 'find' command with appropriate options to search recursively"
        })
        
        # Question 5: File content
        secret_file = list(self.quiz_data['specific_content'].values())[0]  # secret_code.txt
        secret_content = secret_file['content'].strip()
        self.questions.append({
            'question': f"What is the content of the file 'secret_code.txt' in the temp directory?",
            'answer': secret_content,
            'type': 'content',
            'hint': "Use 'cat' command to view file contents"
        })
        
        # Question 6: File extension count
        txt_files = [f for f in self.quiz_data['files'] if f['name'].endswith('.txt')]
        self.questions.append({
            'question': f"How many .txt files are in the entire directory structure?",
            'answer': str(len(txt_files) + 1),  # +1 for secret_code.txt
            'type': 'count',
            'hint': "Use 'find' command to search for files with .txt extension"
        })
        
        # Question 7: Largest file
        all_files = list(self.quiz_data['files']) + list(self.quiz_data['specific_content'].values())
        largest_file = max(all_files, key=lambda x: x.get('size', 0))
        largest_name = largest_file.get('name', os.path.basename(largest_file.get('path', '')))
        self.questions.append({
            'question': f"What is the name of the largest file in the directory structure?",
            'answer': largest_name,
            'type': 'filename',
            'hint': "Use 'find' with 'ls -la' or 'du' commands to compare file sizes"
        })
        
        # Question 8: Directory with most files
        dir_counts = {}
        for file_info in self.quiz_data['files']:
            dir_name = file_info['directory'].split('/')[0]  # Get top-level directory
            dir_counts[dir_name] = dir_counts.get(dir_name, 0) + 1
            
        most_files_dir = max(dir_counts.items(), key=lambda x: x[1])[0]
        self.questions.append({
            'question': f"Which top-level directory contains the most files? (documents, projects, backup, config, or temp)",
            'answer': most_files_dir,
            'type': 'directory',
            'hint': "Count files in each main directory"
        })
        
        print(f"✅ Generated {len(self.questions)} questions")
        
    def create_gui(self):
        """Create the dual-window GUI interface"""
        self.root = tk.Tk()
        self.root.title("Linux Navigation Quiz")
        self.root.geometry("1000x700")
        
        # Create main paned window (top/bottom split)
        main_paned = ttk.PanedWindow(self.root, orient=tk.VERTICAL)
        main_paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Top frame - Instructions/Questions
        self.instruction_frame = ttk.LabelFrame(main_paned, text="Quiz Instructions", padding=10)
        main_paned.add(self.instruction_frame, weight=1)
        
        # Question display
        self.question_label = tk.Label(
            self.instruction_frame, 
            text="Welcome to Linux Navigation Quiz!", 
            font=("Arial", 12),
            wraplength=900,
            justify=tk.LEFT
        )
        self.question_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Answer input frame
        answer_frame = ttk.Frame(self.instruction_frame)
        answer_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(answer_frame, text="Your Answer:").pack(side=tk.LEFT)
        self.answer_entry = ttk.Entry(answer_frame, font=("Arial", 11))
        self.answer_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 10))
        
        self.submit_button = ttk.Button(answer_frame, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(side=tk.RIGHT)
        
        # Progress display
        self.progress_label = tk.Label(
            self.instruction_frame, 
            text="Question 0/0", 
            font=("Arial", 10),
            fg="blue"
        )
        self.progress_label.pack(anchor=tk.W, pady=(10, 0))
        
        # Bottom frame - Live Shell
        self.shell_frame = ttk.LabelFrame(main_paned, text="Live Shell (Navigate Here)", padding=5)
        main_paned.add(self.shell_frame, weight=2)
        
        # Shell output area
        self.shell_text = scrolledtext.ScrolledText(
            self.shell_frame, 
            height=15, 
            font=("Consolas", 10),
            bg="black",
            fg="green",
            insertbackground="green"
        )
        self.shell_text.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        
        # Shell input
        shell_input_frame = ttk.Frame(self.shell_frame)
        shell_input_frame.pack(fill=tk.X)
        
        ttk.Label(shell_input_frame, text="$").pack(side=tk.LEFT)
        self.shell_entry = ttk.Entry(shell_input_frame, font=("Consolas", 10))
        self.shell_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 5))
        self.shell_entry.bind("<Return>", self.execute_shell_command)
        
        # Control buttons
        control_frame = ttk.Frame(self.shell_frame)
        control_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Button(control_frame, text="Clear Shell", command=self.clear_shell).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(control_frame, text="Show Hint", command=self.show_hint).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(control_frame, text="Reset to Quiz Directory", command=self.reset_directory).pack(side=tk.LEFT)
        
        # Bind Enter key for answer submission
        self.answer_entry.bind("<Return>", lambda e: self.submit_answer())
        
        # Initialize shell
        self.initialize_shell()
        
        # Start first question
        self.show_question()
        
    def initialize_shell(self):
        """Initialize the shell in the quiz directory"""
        quiz_path = os.path.abspath(self.quiz_directory)
        self.shell_text.insert(tk.END, f"Linux Navigation Quiz Shell\n")
        self.shell_text.insert(tk.END, f"Quiz Directory: {quiz_path}\n")
        self.shell_text.insert(tk.END, f"Use standard Linux commands to navigate and explore.\n")
        self.shell_text.insert(tk.END, f"Current directory: {quiz_path}\n\n")
        self.shell_text.insert(tk.END, f"$ ")
        self.shell_text.see(tk.END)
        
        # Set working directory for shell commands
        os.chdir(quiz_path)
        
    def execute_shell_command(self, event=None):
        """Execute shell command and display result"""
        command = self.shell_entry.get().strip()
        if not command:
            return
            
        self.shell_entry.delete(0, tk.END)
        
        # Add command to shell display
        self.shell_text.insert(tk.END, f"{command}\n")
        
        try:
            # Execute command
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10,
                cwd=os.getcwd()
            )
            
            # Display output
            if result.stdout:
                self.shell_text.insert(tk.END, result.stdout)
            if result.stderr:
                self.shell_text.insert(tk.END, f"Error: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            self.shell_text.insert(tk.END, "Command timed out\n")
        except Exception as e:
            self.shell_text.insert(tk.END, f"Error: {str(e)}\n")
            
        # Add new prompt
        self.shell_text.insert(tk.END, f"\n$ ")
        self.shell_text.see(tk.END)
        
    def clear_shell(self):
        """Clear the shell output"""
        self.shell_text.delete(1.0, tk.END)
        self.shell_text.insert(tk.END, "$ ")
        
    def reset_directory(self):
        """Reset shell to quiz directory"""
        quiz_path = os.path.abspath(self.quiz_directory)
        os.chdir(quiz_path)
        self.shell_text.insert(tk.END, f"cd {quiz_path}\n$ ")
        self.shell_text.see(tk.END)
        
    def show_hint(self):
        """Show hint for current question"""
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            hint = question.get('hint', 'No hint available')
            messagebox.showinfo("Hint", hint)
            
    def show_question(self):
        """Display current question"""
        if self.current_question >= len(self.questions):
            self.complete_quiz()
            return
            
        question = self.questions[self.current_question]
        question_text = f"Question {self.current_question + 1}:\n\n{question['question']}"
        
        self.question_label.config(text=question_text)
        self.progress_label.config(text=f"Question {self.current_question + 1}/{len(self.questions)}")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()
        
    def submit_answer(self):
        """Submit and verify answer"""
        if self.current_question >= len(self.questions):
            return
            
        user_answer = self.answer_entry.get().strip()
        if not user_answer:
            messagebox.showwarning("Warning", "Please enter an answer")
            return
            
        question = self.questions[self.current_question]
        correct_answer = question['answer']
        
        # Store answer
        self.answers[self.current_question] = {
            'question': question['question'],
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'correct': user_answer.lower() == correct_answer.lower()
        }
        
        # Check if correct
        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!", f"✅ Correct! The answer is: {correct_answer}")
            self.score += 1
        else:
            messagebox.showerror("Incorrect", f"❌ Incorrect. The correct answer is: {correct_answer}")
            
        # Move to next question
        self.current_question += 1
        self.show_question()
        
    def complete_quiz(self):
        """Complete the quiz and generate verification code"""
        # Calculate final score
        total_questions = len(self.questions)
        percentage = (self.score / total_questions) * 100 if total_questions > 0 else 0
        
        # Generate verification code
        verification_code = self.generate_verification_code()
        
        # Show results
        result_text = f"""
Quiz Complete!

Score: {self.score}/{total_questions} ({percentage:.1f}%)

Verification Code: {verification_code}

Please submit this code to your instructor for grading.
        """
        
        self.question_label.config(text=result_text)
        self.submit_button.config(text="Quiz Complete", state="disabled")
        self.answer_entry.config(state="disabled")
        
        messagebox.showinfo("Quiz Complete", f"Quiz finished!\n\nYour verification code is: {verification_code}\n\nPlease submit this code for grading.")
        
    def generate_verification_code(self) -> str:
        """Generate 5-character hex verification code"""
        # Create verification string from quiz data
        verification_data = f"{self.student_id}:{self.assignment_key}:{self.score}:{len(self.questions)}"
        
        # Add answer details to make code unique
        for i, answer_data in self.answers.items():
            verification_data += f":{answer_data['correct']}"
            
        # Generate hash and take first 5 hex characters
        hash_object = hashlib.md5(verification_data.encode())
        return hash_object.hexdigest()[:5].upper()
        
    def run(self):
        """Run the quiz"""
        print("🧭 Starting Linux Navigation Quiz...")
        
        # Setup student session
        if not self.setup_student_session():
            return
            
        # Generate file structure and questions
        print("\n📁 Generating quiz environment...")
        self.generate_file_structure()
        self.generate_questions()
        
        print("\n🎯 Starting GUI interface...")
        print("Navigate using the shell window to answer questions in the instruction window.")
        
        # Create and run GUI
        self.create_gui()
        self.root.mainloop()

if __name__ == "__main__":
    quiz = LinuxNavigationQuiz()
    quiz.run()
