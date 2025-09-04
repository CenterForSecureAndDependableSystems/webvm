#!/usr/bin/env python3
"""
Linux Navigation Quiz - Text-Only Interface with Colors
Interactive quiz for web browser environments without GUI
"""

import os
import sys
import subprocess
import hashlib
import random
import time
import datetime

class Colors:
    """ANSI color codes for background changes without clearing screen"""
    # Background modes without clearing screen
    WHITE_MODE = '\033[47m\033[30m'    # White background, black text
    BLACK_MODE = '\033[40m\033[32m'    # Black background, green text
    RESET = '\033[0m'
    
    # Simple status colors (no background change)
    SUCCESS = '\033[32m'     # Green text
    ERROR = '\033[31m'       # Red text  
    WARNING = '\033[33m'     # Yellow text
    YELLOW = '\033[33m'      # Yellow text (same as WARNING)
    PROGRESS = '\033[36m'    # Cyan text for progress messages

def clear_screen():
    """Set white background mode without clearing screen"""
    # Get terminal width and fill the current line with white background
    try:
        import shutil
        width = shutil.get_terminal_size().columns
        print(f'{Colors.WHITE_MODE}{" " * width}', end='\r')
    except:
        print(Colors.WHITE_MODE, end='')

def clear_screen_completely():
    """Clear screen completely and set white background mode"""
    print('\033[2J\033[H', end='')  # Clear screen and home cursor
    print(Colors.WHITE_MODE, end='')
    # Fill initial screen with white background
    try:
        import shutil
        width = shutil.get_terminal_size().columns
        height = shutil.get_terminal_size().lines
        for _ in range(height):
            print(f'{" " * width}')
        print('\033[H', end='')  # Return to top
    except:
        pass

def enter_shell_mode():
    """Switch to black background shell mode without clearing screen"""
    print(Colors.BLACK_MODE, end='')

def exit_shell_mode():
    """Return to white background mode without clearing screen"""
    print(Colors.WHITE_MODE, end='')

def print_white_bg(text="", end='\n'):
    """Print text with white background that extends across full line"""
    try:
        import shutil
        width = shutil.get_terminal_size().columns
        
        # Always ensure we're in white mode first
        print(Colors.WHITE_MODE, end='')
        
        if text:
            # Calculate actual display length (excluding ANSI codes)
            import re
            # Remove ANSI escape sequences for length calculation
            display_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
            text_len = len(display_text)
            
            if text_len < width:
                spaces_needed = width - text_len
                # Print text with white background, then fill rest with spaces
                print(f'{Colors.WHITE_MODE}{text}{" " * spaces_needed}', end=end)
            else:
                # Text is longer than width, just print with white background
                print(f'{Colors.WHITE_MODE}{text}', end=end)
        else:
            # Just print a full line of spaces for empty lines
            print(f'{Colors.WHITE_MODE}{" " * width}', end=end)
            
        # Ensure we end with white mode for next line
        if end == '\n':
            print(Colors.WHITE_MODE, end='')
            
    except:
        # Fallback if terminal size detection fails
        print(f'{Colors.WHITE_MODE}{text}', end=end)

def print_black_bg(text="", end='\n'):
    """Print text with black background that extends across full line"""
    try:
        import shutil
        width = shutil.get_terminal_size().columns
        
        # Always ensure we're in black mode first
        print(Colors.BLACK_MODE, end='')
        
        if text:
            # Calculate actual display length (excluding ANSI codes)
            import re
            # Remove ANSI escape sequences for length calculation
            display_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
            text_len = len(display_text)
            
            if text_len < width:
                spaces_needed = width - text_len
                # Print text with black background, then fill rest with spaces
                print(f'{Colors.BLACK_MODE}{text}{" " * spaces_needed}', end=end)
            else:
                # Text is longer than width, just print with black background
                print(f'{Colors.BLACK_MODE}{text}', end=end)
        else:
            # Just print a full line of spaces for empty lines
            print(f'{Colors.BLACK_MODE}{" " * width}', end=end)
            
        # Reset to default after printing
        if end == '\n':
            print(Colors.RESET, end='')
            
    except:
        # Fallback if terminal size detection fails
        print(f'{Colors.BLACK_MODE}{text}{Colors.RESET}', end=end)

class LinuxNavigationQuizTextOnly:
    """
    Text-only Linux navigation quiz for web browser environments
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
        
    def print_header(self, title, width=60):
        """Print a formatted header with white background"""
        print_white_bg(f"{'=' * width}")
        print_white_bg(f"{title:^{width}}")
        print_white_bg(f"{'=' * width}")
        
    def print_section(self, title, width=50):
        """Print a section header with white background"""
        print_white_bg(f"{'-' * width}")
        print_white_bg(f"📋 {title}")
        print_white_bg(f"{'-' * width}")
        
    def setup_student_session(self):
        """Setup student information and assignment key"""
        # White background already set by main(), no need to clear again
        self.print_header("🧭 Linux Navigation Quiz", 60)
        print_white_bg("Welcome to the interactive Linux file navigation assessment!")
        print_white_bg("You will navigate a custom file structure using real Linux commands.")
        print_white_bg()
        print_white_bg("Instructions:")
        print_white_bg("• Answer 8 questions about file locations and properties")
        print_white_bg("• Use shell commands to explore the generated file structure")
        print_white_bg("• Type your answers exactly as requested")
        print_white_bg("• Get immediate feedback on each answer")
        
        self.print_section("👤 Student Information Setup")
        
        while not self.student_id:
            self.student_id = input(f"{Colors.WHITE_MODE}Enter your student ID or email: ").strip()
            if not self.student_id:
                print_white_bg(f"{Colors.ERROR}❌ Student ID is required. Please try again.{Colors.RESET}")
                
        while not self.assignment_key:
            self.assignment_key = input(f"{Colors.WHITE_MODE}Enter assignment key (from instructor): ").strip()
            if not self.assignment_key:
                print_white_bg(f"{Colors.ERROR}❌ Assignment key is required. Please try again.{Colors.RESET}")
                
        print_white_bg(f"✅ Student: {self.student_id}")
        print_white_bg(f"✅ Assignment: {self.assignment_key}")
        print_white_bg(f"✅ Setup complete!")
        return True
        
    def generate_file_structure(self):
        """Generate unique file structure based on student ID and assignment key"""
        clear_screen()  # Set white background without clearing
        self.print_section("🔧 Generating Your Unique Quiz Environment")
        
        # Create deterministic random seed from student info
        seed_string = f"{self.student_id}:{self.assignment_key}"
        seed = int(hashlib.md5(seed_string.encode()).hexdigest()[:8], 16)
        random.seed(seed)
        
        print_white_bg("Creating file structure based on your student ID...")
        
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
        
        # Generate regular files
        file_templates = [
            ("documents/readme{}.txt", "readme", "This is a readme file for {student_id}\nGenerated on {timestamp}\nAssignment: {assignment_key}"),
            ("documents/reports/report{}.doc", "report", "Monthly Report Document\nStudent: {student_id}\nData analysis results..."),
            ("projects/web/index{}.html", "index", "<html><body><h1>Student Project</h1><p>Created by {student_id}</p></body></html>"),
            ("projects/mobile/app{}.py", "app", "#!/usr/bin/env python3\n# Mobile app by {student_id}\nprint('Hello World')"),
            ("backup/weekly/backup{}.tar", "backup", "Binary backup file content (simulated)\nCreated: {timestamp}"),
            ("backup/daily/size_test.log", "log", "Size test log file\nStudent: {student_id}\nFile size tests completed successfully."),
            ("config/config{}.conf", "config", "[settings]\nstudent_id={student_id}\nassignment={assignment_key}\ntimestamp={timestamp}"),
            ("temp/notes{}.txt", "notes", "Temporary notes file\nStudent work in progress\nDo not delete!"),
            ("temp/secret_code.txt", "secret", f"SECRET_CODE_{random.randint(1000, 9999)}")
        ]
        
        # Generate hidden files
        hidden_templates = [
            (".profile", "Profile settings for {student_id}"),
            ("config/.hidden_config", "Hidden configuration\nSecret settings here")
        ]
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create regular files
        for template_path, file_type, content_template in file_templates:
            if "{}" in template_path:
                number = random.randint(10, 99)
                file_path = template_path.format(number)
                file_key = f"{file_type}{number}"
            else:
                file_path = template_path
                file_key = file_type
                
            full_path = os.path.join(self.quiz_directory, file_path)
            
            # Generate content
            content = content_template.format(
                student_id=self.student_id,
                assignment_key=self.assignment_key,
                timestamp=timestamp
            )
            
            # Write file
            with open(full_path, 'w') as f:
                f.write(content)
                
            # Store file info
            file_info = {
                'path': file_path,
                'name': os.path.basename(file_path),
                'size': len(content.encode('utf-8')),
                'type': file_type,
                'key': file_key
            }
            self.quiz_data['files'].append(file_info)
            
        # Create hidden files
        for hidden_path, content_template in hidden_templates:
            full_path = os.path.join(self.quiz_directory, hidden_path)
            content = content_template.format(student_id=self.student_id)
            
            with open(full_path, 'w') as f:
                f.write(content)
                
            file_info = {
                'path': hidden_path,
                'name': os.path.basename(hidden_path),
                'size': len(content.encode('utf-8')),
                'type': 'hidden'
            }
            self.quiz_data['hidden_files'].append(file_info)
            
        print_white_bg(f"✅ Generated {len(self.quiz_data['files'])} files")
        print_white_bg(f"✅ Generated {len(self.quiz_data['hidden_files'])} hidden files")
        print_white_bg(f"✅ Generated {len(directories)} directories")
        print_white_bg(f"✅ Quiz environment ready in '{self.quiz_directory}/' directory")
        
    def generate_questions(self):
        """Generate quiz questions based on the file structure"""
        clear_screen()  # Set white background without clearing
        self.print_section("Generating Quiz Questions")
        
        # Analyze the generated structure for question answers
        self.analyze_file_structure()
        
        question_templates = [
            {
                'type': 'file_path',
                'question': f"What is the relative path to the file named '{self.quiz_data['target_file']['name']}'? (Answer without leading ./)",
                'answer': self.quiz_data['target_file']['path'],
                'hint': "Use: find . -name 'filename' (remove the ./ from the result)"
            },
            {
                'type': 'file_count',
                'question': f"How many files are in the '{self.quiz_data['target_directory']}' directory (not including subdirectories)?",
                'answer': str(self.quiz_data['files_in_target_dir']),
                'hint': "Use: ls directory_name | wc -l"
            },
            {
                'type': 'file_size',
                'question': f"What is the size in bytes of the file '{self.quiz_data['size_test_file']['name']}'?",
                'answer': str(self.quiz_data['size_test_file']['size']),
                'hint': "Use: ls -l filename or du -b filename"
            },
            {
                'type': 'hidden_files',
                'question': "How many hidden files (names starting with '.') exist in the entire quiz structure?",
                'answer': str(len(self.quiz_data['hidden_files'])),
                'hint': "Use: find . -name '.*' -type f | wc -l"
            },
            {
                'type': 'file_content',
                'question': "What is the content of the file 'secret_code.txt'?",
                'answer': self.quiz_data['secret_content'],
                'hint': "Use: cat temp/secret_code.txt"
            },
            {
                'type': 'file_extension',
                'question': "How many files with the '.txt' extension exist in total?",
                'answer': str(self.quiz_data['txt_file_count']),
                'hint': "Use: find . -name '*.txt' | wc -l"
            },
            {
                'type': 'largest_file',
                'question': "What is the name of the largest file in the entire structure?",
                'answer': self.quiz_data['largest_file']['name'],
                'hint': "Use: find . -type f -exec ls -la {} + | sort -k5 -n"
            },
            {
                'type': 'directory_comparison',
                'question': f"Which directory contains more files: 'documents' or 'projects'?",
                'answer': self.quiz_data['busiest_directory'],
                'hint': "Count files in each directory and compare"
            }
        ]
        
        self.questions = question_templates
        print(f"✅ Generated {len(self.questions)} questions")
        print("✅ Questions are ready!")
        
    def analyze_file_structure(self):
        """Analyze the generated structure to create question answers"""
        # Find target file for path question
        regular_files = [f for f in self.quiz_data['files'] if f['type'] != 'secret']
        self.quiz_data['target_file'] = random.choice(regular_files)
        
        # Find target directory for counting
        self.quiz_data['target_directory'] = 'documents'
        files_in_docs = [f for f in self.quiz_data['files'] if f['path'].startswith('documents/') and '/' not in f['path'][10:]]
        self.quiz_data['files_in_target_dir'] = len(files_in_docs)
        
        # Find size test file
        size_files = [f for f in self.quiz_data['files'] if 'size_test' in f['name']]
        if size_files:
            self.quiz_data['size_test_file'] = size_files[0]
        else:
            self.quiz_data['size_test_file'] = random.choice(self.quiz_data['files'])
            
        # Get secret content
        secret_path = os.path.join(self.quiz_directory, 'temp/secret_code.txt')
        if os.path.exists(secret_path):
            with open(secret_path, 'r') as f:
                self.quiz_data['secret_content'] = f.read().strip()
        
        # Count txt files
        txt_files = [f for f in self.quiz_data['files'] + self.quiz_data['hidden_files'] if f['name'].endswith('.txt')]
        self.quiz_data['txt_file_count'] = len(txt_files)
        
        # Find largest file
        all_files = self.quiz_data['files'] + self.quiz_data['hidden_files']
        largest = max(all_files, key=lambda f: f['size'])
        self.quiz_data['largest_file'] = largest
        
        # Compare directory file counts
        docs_count = len([f for f in self.quiz_data['files'] if f['path'].startswith('documents/')])
        projects_count = len([f for f in self.quiz_data['files'] if f['path'].startswith('projects/')])
        self.quiz_data['busiest_directory'] = 'documents' if docs_count > projects_count else 'projects'
        
    def run_shell_command(self, command):
        """Execute a shell command in the quiz directory and return output"""
        try:
            # Change to quiz directory for command execution
            result = subprocess.run(
                command,
                shell=True,
                cwd=self.quiz_directory,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                return result.stdout
            else:
                return f"Error: {result.stderr}"
                
        except subprocess.TimeoutExpired:
            return "Error: Command timed out"
        except Exception as e:
            return f"Error: {str(e)}"
            
    def show_shell_help(self):
        """Display shell command help"""
        print("\n📚 Useful Commands for Navigation:")
        print("  ls              - List files in current directory")
        print("  ls -la          - List all files (including hidden) with details")
        print("  cd <directory>  - Change to directory")
        print("  cd ..           - Go up one directory level")
        print("  pwd             - Show current directory path")
        print("  find . -name 'filename' - Find files by name")
        print("  find . -name '*.txt'    - Find files by extension")
        print("  cat <filename>  - Show file contents")
        print("  wc -l <file>    - Count lines in file")
        print("  ls | wc -l      - Count files in directory")
        print("  du -b <file>    - Show file size in bytes")
        print("  ls -la <file>   - Show file details including size")
        print("\n� Quiz Commands:")
        print("  question        - Show current question and hint again")
        print("  help            - Show this help message")
        print("  exit            - Return to quiz interface")
        print("\n�💡 Tip: You can run commands while answering questions!")
        
    def interactive_shell(self, question_text=None, hint_text=None, question_num=None):
        """Provide an interactive shell session with full black background"""
        # Switch to shell mode (black background, green text)
        enter_shell_mode()
        
        print(f"\n🐚 Interactive Shell - Quiz Directory: {self.quiz_directory}")
        print("Type 'exit' to return to quiz, 'help' for commands, 'question' to see current question")
        print("-" * 50)
        
        while True:
            try:
                command = input(f"quiz:{self.quiz_directory}$ ").strip()
                
                if command.lower() == 'exit':
                    break
                elif command.lower() == 'help':
                    self.show_shell_help()
                    continue
                elif command.lower() == 'question' and question_text:
                    # Redisplay the current question context
                    print("=" * 60)
                    print(f"CURRENT QUESTION {question_num + 1}:")
                    print(f"📝 {question_text}")
                    print(f"💡 Hint: {hint_text}")
                    print("=" * 60)
                    continue
                elif command == '':
                    continue
                    
                output = self.run_shell_command(command)
                if output.strip():
                    print(output)
                    
            except KeyboardInterrupt:
                print("\n^C")
                break
            except EOFError:
                break
                
        # Return to white background mode without clearing
        exit_shell_mode()
        print("Returned to quiz interface.")
        
    def present_question(self, question_num):
        """Present a single question to the student"""
        question = self.questions[question_num]
        
        clear_screen()  # Set white background without clearing
        self.print_header(f"Question {question_num + 1} of {len(self.questions)}")
        print_white_bg(f"📝 {question['question']}")
        print_white_bg()
        print_white_bg(f"💡 Hint: {question['hint']}")
        print_white_bg()
        print_white_bg("Options:")
        print_white_bg("  1. Type your answer")
        print_white_bg("  2. Open shell to explore (type 'shell')")
        print_white_bg("  3. Show hint again (type 'hint')")
        print_white_bg("  4. Quit quiz (type 'quit' or 'exit')")
        
        while True:
            print_white_bg()
            print_white_bg("="*50)
            user_input = input(f"{Colors.WHITE_MODE}Your answer (or 'shell'/'hint'/'quit'): ").strip()
            
            if user_input.lower() == 'shell':
                self.interactive_shell(
                    question_text=question['question'],
                    hint_text=question['hint'],
                    question_num=question_num
                )
                # After returning from shell, set white background without clearing
                exit_shell_mode()
                print_white_bg()
                print_white_bg(f"📝 Question {question_num + 1}: {question['question']}")
                print_white_bg(f"💡 Hint: {question['hint']}")
                continue
            elif user_input.lower() == 'hint':
                print_white_bg(f"💡 Hint: {question['hint']}")
                continue
            elif user_input.lower() in ['quit', 'exit']:
                print_white_bg()
                print_white_bg(f"⚠️ Quiz terminated by user.")
                print_white_bg(f"📊 Final Progress: {self.score}/{question_num + 1} questions attempted")
                print_white_bg(f"🎯 Final score: {self.score}/{question_num + 1}")
                print_white_bg("Thank you for participating!")
                
                # Print one blank line with full-width black background
                print_black_bg()
                
                return 'quit'  # Return 'quit' to signal termination
            elif user_input == '':
                print_white_bg(f"Please enter an answer.")
                continue
            else:
                # Check answer
                correct = self.check_answer(question, user_input)
                if correct:
                    print_white_bg(f"✅ Correct!")
                    self.score += 1
                    self.answers[question_num] = True
                else:
                    print_white_bg(f"❌ Incorrect. The correct answer was: {question['answer']}")
                    self.answers[question_num] = False
                    
                # Show progress
                print_white_bg()
                print_white_bg(f"📊 Progress: {question_num + 1}/{len(self.questions)} questions completed")
                print_white_bg(f"🎯 Current score: {self.score}/{question_num + 1}")
                
                input(f"\n{Colors.WHITE_MODE}Press Enter to continue to next question...")
                break
                
        return 'continue'  # Return 'continue' to signal normal completion
                
    def check_answer(self, question, user_answer):
        """Check if the user's answer is correct"""
        correct_answer = question['answer'].lower().strip()
        user_answer = user_answer.lower().strip()
        
        # Handle path answers - accept both with and without leading ./
        if question['type'] == 'file_path':
            correct_answer = correct_answer.lstrip('./')
            user_answer = user_answer.lstrip('./')
            
        return correct_answer == user_answer
        
    def run_quiz(self):
        """Run the complete quiz"""
        clear_screen()  # Set white background without clearing
        self.print_header("🚀 Starting Quiz")
        
        print("You are now ready to begin the quiz!")
        print("The file structure has been generated in the 'QuizEnvironment' directory.")
        print("You can explore it using shell commands between questions.")
        
        # Show initial structure overview
        print(f"\n📁 Your quiz environment contains:")
        output = self.run_shell_command("find . -type d | head -10")
        print("Directories:")
        print(output)
        
        output = self.run_shell_command("find . -type f | wc -l")
        print(f"Total files: {output.strip()}")
        
        input("\nPress Enter to begin the quiz...")
        
        # Run through all questions
        for i in range(len(self.questions)):
            self.current_question = i
            result = self.present_question(i)
            
            # Check if user quit the quiz
            if result == 'quit':
                return  # Exit the entire quiz
            
        # Show final results only if quiz completed normally
        self.show_final_results()
        
    def show_final_results(self):
        """Display final quiz results and verification code"""
        clear_screen()  # Set white background without clearing
        self.print_header("🎉 Quiz Complete!")
        
        percentage = (self.score / len(self.questions)) * 100
        
        print(f"📊 Final Score: {self.score}/{len(self.questions)} ({percentage:.1f}%)")
        print(f"👤 Student: {self.student_id}")
        print(f"📝 Assignment: {self.assignment_key}")
        print(f"📅 Completed: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Generate verification code
        verification_code = self.generate_verification_code()
        
        print(f"\n{Colors.SUCCESS}🔑 Your Verification Code: {verification_code}{Colors.RESET}")
        print("=" * 50)
        print(f"{Colors.WARNING}📋 IMPORTANT: Submit this verification code to your instructor!{Colors.RESET}")
        print("This code proves you completed the quiz and shows your score.")
        print("=" * 50)
        
        # Show score breakdown
        print(f"\n📈 Score Breakdown:")
        for i, (question_num, correct) in enumerate(self.answers.items()):
            status = f"{Colors.SUCCESS}✅{Colors.RESET}" if correct else f"{Colors.ERROR}❌{Colors.RESET}"
            print(f"  Question {question_num + 1}: {status}")
            
        print(f"\nThank you for completing the Linux Navigation Quiz!")
        
    def generate_verification_code(self):
        """Generate a verification code based on student performance"""
        # Create verification string
        verification_data = f"{self.student_id}:{self.assignment_key}:{self.score}:{len(self.questions)}"
        
        # Add answer pattern
        for i in range(len(self.questions)):
            correct = self.answers.get(i, False)
            verification_data += f":{correct}"
            
        # Generate MD5 hash and take first 5 characters
        code = hashlib.md5(verification_data.encode()).hexdigest()[:5].upper()
        return code
        
    def main(self):
        """Main quiz execution"""
        try:
            # Setup student session (screen already cleared by module main())
            if not self.setup_student_session():
                return
                
            # Generate unique file structure
            self.generate_file_structure()
            
            # Generate questions based on structure
            self.generate_questions()
            
            # Run the quiz
            self.run_quiz()
            
        except KeyboardInterrupt:
            print("\n\n⚠️ Quiz interrupted by user.")
            print("Your progress has not been saved.")
        except Exception as e:
            print(f"\n{Colors.ERROR}❌ An error occurred: {str(e)}{Colors.RESET}")
            print(f"{Colors.WARNING}Please contact your instructor for assistance.{Colors.RESET}")

def main():
    """Entry point for the quiz"""
    # Clear screen completely at program start
    clear_screen_completely()
    
    quiz = LinuxNavigationQuizTextOnly()
    quiz.main()

if __name__ == "__main__":
    main()
