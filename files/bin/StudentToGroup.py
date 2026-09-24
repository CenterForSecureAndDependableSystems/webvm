#!/usr/bin/env python3
"""
Group Hash Generator for Linux Tutorial
Generates group assignments and progress codes for LMS integration
"""

import random
import hashlib
import csv
from typing import List, Dict

class GroupHashGenerator:
    """
    Utility to generate group assignments and progress codes for the Linux Tutorial.
    
    This tool helps instructors create answer keys for their Learning Management System
    by generating all possible progress codes and student group assignments.
    """
    
    def __init__(self):
        self.num_groups = 5
        self.progress_checkpoint = 5  # Same as in tutorial.py
        self.group_names = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']
        self.assignment_key = None  # Will be set when generating codes

    def set_assignment_key(self, assignment_key: str) -> None:
        """Set the assignment key for generating unique code sets"""
        self.assignment_key = assignment_key
        print(f"🔑 Assignment key set to: '{assignment_key}'")

    def get_student_group(self, student_id: str) -> int:
        """Assign student to one of 5 groups based on their student ID"""
        # Use hash of student ID to consistently assign to groups 1-5
        group_hash = hash(student_id) % self.num_groups
        return group_hash + 1  # Groups 1-5 instead of 0-4
    
    def get_student_group_letter(self, student_id: str) -> str:
        """Get the group letter (A-E) for a student"""
        group_num = self.get_student_group(student_id)
        return self.group_names[group_num - 1]
    
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
    
    def generate_student_groups_csv(self, student_file: str, output_file: str = "student_groups.csv") -> None:
        """Generate CSV file showing which students are in which groups"""
        students = self.read_student_list(student_file)
        
        if not students:
            return
        
        # Organize students by group
        groups = {group_name: [] for group_name in self.group_names}
        
        for student in students:
            group_name = self.get_student_group_letter(student)
            groups[group_name].append(student)
        
        # Find the maximum number of students in any group (for CSV columns)
        max_students = max(len(group_students) for group_students in groups.values())
        
        # Write CSV file
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header row
            header = []
            for group_name in self.group_names:
                header.extend([group_name, ''])  # Group name followed by empty column
            writer.writerow(header)
            
            # Write student rows
            for i in range(max_students):
                row = []
                for group_name in self.group_names:
                    if i < len(groups[group_name]):
                        row.extend([groups[group_name][i], ''])  # Student email followed by empty column
                    else:
                        row.extend(['', ''])  # Empty cells if no more students in this group
                writer.writerow(row)
        
        print(f"📁 Student groups CSV generated: {output_file}")
        
        # Print summary
        print("\n📊 GROUP DISTRIBUTION:")
        print("-" * 40)
        for group_name in self.group_names:
            count = len(groups[group_name])
            print(f"{group_name}: {count} students")
        print(f"Total: {len(students)} students")
    
    def generate_progress_code(self, group_number: int, exercise_count: int, assignment_key: str = None) -> str:
        """Generate a 5-character progress code for a specific group with assignment key"""
        # Use provided assignment key or the instance variable
        key = assignment_key or self.assignment_key or "DEFAULT"
        
        # Create a seed based on assignment key, group number and exercise count
        seed_string = f"ASSIGNMENT-{key}-GROUP{group_number}-{exercise_count}"
        
        # Convert string to numeric seed
        seed_value = hash(seed_string) % (2**32)
        
        # Seed the random number generator
        random.seed(seed_value)
        
        # Generate 5-character alphanumeric code
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        progress_code = ''.join(random.choices(characters, k=5))
        
        return progress_code
    
    def generate_answer_key_csv(self, max_exercises: int = 20, filename: str = "answer_key.csv", assignment_key: str = None) -> None:
        """Generate CSV file with answer keys for all groups"""
        # Set assignment key if provided
        if assignment_key:
            self.set_assignment_key(assignment_key)
        
        # Get the current assignment key
        current_key = self.assignment_key or "DEFAULT"
        
        checkpoints = list(range(self.progress_checkpoint, max_exercises + 1, self.progress_checkpoint))
        if max_exercises not in checkpoints:
            checkpoints.append(max_exercises)
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Header with assignment info
            writer.writerow(['Answer Key'])
            writer.writerow(['Assignment Key', current_key])
            writer.writerow(['Max Exercises', max_exercises])
            writer.writerow([])  # Empty row
            
            # Progress codes header
            header = ['Group'] + [f'Checkpoint_{cp}' for cp in checkpoints]
            writer.writerow(header)
            
            # Data rows
            for i, group_name in enumerate(self.group_names, 1):
                row = [group_name]
                for checkpoint in checkpoints:
                    code = self.generate_progress_code(i, checkpoint, current_key)
                    row.append(code)
                writer.writerow(row)
        
        print(f"📁 Answer key CSV generated: {filename}")
        print(f"🔑 Assignment key used: '{current_key}'")
    
    def generate_individual_answer_keys(self, student_file: str, max_exercises: int = 20, output_dir: str = "individual_keys", assignment_key: str = None) -> None:
        """Generate individual answer key files for each student"""
        import os
        
        # Set assignment key if provided
        if assignment_key:
            self.set_assignment_key(assignment_key)
        
        # Get the current assignment key
        current_key = self.assignment_key or "DEFAULT"
        
        students = self.read_student_list(student_file)
        
        if not students:
            return
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"📁 Created directory: {output_dir}")
        
        checkpoints = list(range(self.progress_checkpoint, max_exercises + 1, self.progress_checkpoint))
        if max_exercises not in checkpoints:
            checkpoints.append(max_exercises)
        
        print(f"📝 Generating individual answer keys for {len(students)} students...")
        print(f"🔑 Using assignment key: '{current_key}'")
        
        for student in students:
            group_num = self.get_student_group(student)
            group_letter = self.get_student_group_letter(student)
            
            # Create filename (sanitize email for filename)
            safe_filename = student.replace('@', '_at_').replace('.', '_')
            filename = os.path.join(output_dir, f"{safe_filename}_answer_key.csv")
            
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                
                # Header with student info
                writer.writerow(['Student Answer Key'])
                writer.writerow(['Student ID', student])
                writer.writerow(['Assigned Group', group_letter])
                writer.writerow(['Group Number', group_num])
                writer.writerow(['Assignment Key', current_key])
                writer.writerow([])  # Empty row
                
                # Progress codes header
                writer.writerow(['Exercise Count', 'Progress Code', 'Code Type'])
                
                # Generate codes for each checkpoint
                for checkpoint in checkpoints:
                    code = self.generate_progress_code(group_num, checkpoint, current_key)
                    code_type = "FINAL COMPLETION" if checkpoint == max_exercises else "CHECKPOINT"
                    writer.writerow([checkpoint, code, code_type])
        
        print(f"✅ Generated {len(students)} individual answer key files in '{output_dir}' directory")
        print(f"📊 Files are named: [student_email]_answer_key.csv")

    def generate_master_student_answer_key(self, student_file: str, max_exercises: int = 20, filename: str = "master_answer_key.csv", assignment_key: str = None) -> None:
        """Generate a single CSV with all students and their answer keys"""
        # Set assignment key if provided
        if assignment_key:
            self.set_assignment_key(assignment_key)
        
        # Get the current assignment key
        current_key = self.assignment_key or "DEFAULT"
        
        students = self.read_student_list(student_file)
        
        if not students:
            return
        
        checkpoints = list(range(self.progress_checkpoint, max_exercises + 1, self.progress_checkpoint))
        if max_exercises not in checkpoints:
            checkpoints.append(max_exercises)
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Header with assignment info
            writer.writerow(['Master Answer Key'])
            writer.writerow(['Assignment Key', current_key])
            writer.writerow(['Max Exercises', max_exercises])
            writer.writerow([])  # Empty row
            
            # Main header row
            header = ['Student ID', 'Group'] + [f'Checkpoint_{cp}' for cp in checkpoints]
            writer.writerow(header)
            
            # Data rows for each student
            for student in students:
                group_num = self.get_student_group(student)
                group_letter = self.get_student_group_letter(student)
                
                row = [student, group_letter]
                
                # Add progress codes for this student
                for checkpoint in checkpoints:
                    code = self.generate_progress_code(group_num, checkpoint, current_key)
                    row.append(code)
                
                writer.writerow(row)
    
        print(f"📁 Master answer key generated: {filename}")
        print(f"✅ Contains individual codes for {len(students)} students")
        print(f"🔑 Assignment key used: '{current_key}'")

    def load_student_groups_from_csv(self, filename: str) -> Dict[str, List[str]]:
        """Load student groups from an existing CSV file"""
        try:
            groups = {group_name: [] for group_name in self.group_names}
        
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)  # Skip header row
            
                # Parse header to find group columns
                group_columns = {}
                for i, col_name in enumerate(header):
                    if col_name in self.group_names:
                        group_columns[col_name] = i
            
                # Read student data
                for row in reader:
                    for group_name, col_index in group_columns.items():
                        if col_index < len(row) and row[col_index].strip():
                            student_email = row[col_index].strip()
                            if student_email:  # Only add non-empty entries
                                groups[group_name].append(student_email)
        
            total_students = sum(len(group_students) for group_students in groups.values())
            print(f"✅ Loaded {total_students} students from {filename}")
        
            # Print group distribution
            print("\n📊 LOADED GROUP DISTRIBUTION:")
            print("-" * 40)
            for group_name in self.group_names:
                count = len(groups[group_name])
                print(f"{group_name}: {count} students")
            print(f"Total: {total_students} students")
        
            return groups
        
        except FileNotFoundError:
            print(f"❌ Error: File '{filename}' not found!")
            return {}
        except Exception as e:
            print(f"❌ Error reading CSV file: {e}")
            return {}

    def generate_answer_keys_from_loaded_groups(self, groups: Dict[str, List[str]], max_exercises: int = 20, assignment_key: str = "DEFAULT") -> None:
        """Generate answer keys based on pre-loaded student groups"""
        if not groups or not any(groups.values()):
            print("❌ No student groups loaded!")
            return
    
        checkpoints = list(range(self.progress_checkpoint, max_exercises + 1, self.progress_checkpoint))
        if max_exercises not in checkpoints:
            checkpoints.append(max_exercises)
    
        # Generate group answer key
        group_filename = f"loaded_groups_answer_key_{assignment_key}.csv"
        with open(group_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Header with assignment info
            writer.writerow(['Answer Key (From Loaded Groups)'])
            writer.writerow(['Assignment Key', assignment_key])
            writer.writerow(['Max Exercises', max_exercises])
            writer.writerow([])  # Empty row
            
            # Progress codes header
            header = ['Group'] + [f'Checkpoint_{cp}' for cp in checkpoints]
            writer.writerow(header)
            
            # Data rows
            for i, group_name in enumerate(self.group_names, 1):
                if groups[group_name]:  # Only include groups that have students
                    row = [group_name]
                    for checkpoint in checkpoints:
                        code = self.generate_progress_code(i, checkpoint, assignment_key)
                        row.append(code)
                    writer.writerow(row)
    
        print(f"📁 Group answer key generated: {group_filename}")
    
        # Generate individual student answer keys
        output_dir = f"loaded_individual_keys_{assignment_key}"
        import os
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"📁 Created directory: {output_dir}")
    
        total_students = 0
        for group_name, students in groups.items():
            if not students:
                continue
            
            group_num = self.group_names.index(group_name) + 1
            
            for student in students:
                total_students += 1
                # Create filename (sanitize email for filename)
                safe_filename = student.replace('@', '_at_').replace('.', '_')
                filename = os.path.join(output_dir, f"{safe_filename}_answer_key.csv")
                
                with open(filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    
                    # Header with student info
                    writer.writerow(['Student Answer Key (From Loaded Groups)'])
                    writer.writerow(['Student ID', student])
                    writer.writerow(['Assigned Group', group_name])
                    writer.writerow(['Group Number', group_num])
                    writer.writerow(['Assignment Key', assignment_key])
                    writer.writerow([])  # Empty row
                    
                    # Progress codes header
                    writer.writerow(['Exercise Count', 'Progress Code', 'Code Type'])
                    
                    # Generate codes for each checkpoint
                    for checkpoint in checkpoints:
                        code = self.generate_progress_code(group_num, checkpoint, assignment_key)
                        code_type = "FINAL COMPLETION" if checkpoint == max_exercises else "CHECKPOINT"
                        writer.writerow([checkpoint, code, code_type])
    
        print(f"✅ Generated {total_students} individual answer key files in '{output_dir}' directory")
        print(f"🔑 Assignment key used: '{assignment_key}'")

    def interactive_mode(self):
        """Interactive mode for testing and generating codes"""
        print("🖥️  INTERACTIVE GROUP HASH GENERATOR")
        print("=" * 50)
    
        loaded_groups = {}  # Store loaded groups
    
        while True:
            print(f"\nCurrent Assignment Key: {self.assignment_key or 'Not Set'}")
            if loaded_groups:
                total_loaded = sum(len(students) for students in loaded_groups.values())
                print(f"Loaded Groups: {total_loaded} students in memory")
        
            print("\nChoose an option:")
            print("1. Set assignment key")
            print("2. Generate student groups from file (hash-based)")
            print("3. Load existing student groups from CSV file")
            print("4. Generate answer key CSV (by groups)")
            print("5. Generate individual answer keys (separate files)")
            print("6. Generate master answer key (all students in one file)")
            print("7. Generate answer keys from loaded groups")
            print("8. Test single student ID")
            print("9. Create sample student file")
            print("10. Exit")
        
            choice = input("\nEnter your choice (1-10): ").strip()
        
            if choice == '1':
                assignment_key = input("Enter assignment key (e.g., 'Assignment1', 'Midterm', 'Fall2024'): ").strip()
                if assignment_key:
                    self.set_assignment_key(assignment_key)
                else:
                    print("Assignment key cannot be empty!")
        
            elif choice == '2':
                input_file = input("Student list filename (e.g., students.txt): ").strip()
                output_file = input("Output CSV filename (default: student_groups.csv): ").strip()
                output_file = output_file if output_file else "student_groups.csv"
                self.generate_student_groups_csv(input_file, output_file)
        
            elif choice == '3':
                input_file = input("Student groups CSV filename: ").strip()
                loaded_groups = self.load_student_groups_from_csv(input_file)
                if loaded_groups:
                    print("✅ Student groups loaded successfully!")
                    print("   You can now use option 7 to generate answer keys from these groups.")
        
            elif choice == '4':
                max_ex = input("Maximum exercises (default 20): ").strip()
                max_ex = int(max_ex) if max_ex else 20
                filename = input("CSV filename (default answer_key.csv): ").strip()
                filename = filename if filename else "answer_key.csv"
                assignment_key = input("Assignment key (Enter to use current): ").strip()
                assignment_key = assignment_key if assignment_key else None
                self.generate_answer_key_csv(max_ex, filename, assignment_key)
        
            elif choice == '5':
                input_file = input("Student list filename: ").strip()
                max_ex = input("Maximum exercises (default 20): ").strip()
                max_ex = int(max_ex) if max_ex else 20
                output_dir = input("Output directory (default: individual_keys): ").strip()
                output_dir = output_dir if output_dir else "individual_keys"
                assignment_key = input("Assignment key (Enter to use current): ").strip()
                assignment_key = assignment_key if assignment_key else None
                self.generate_individual_answer_keys(input_file, max_ex, output_dir, assignment_key)
        
            elif choice == '6':
                input_file = input("Student list filename: ").strip()
                max_ex = input("Maximum exercises (default 20): ").strip()
                max_ex = int(max_ex) if max_ex else 20
                filename = input("CSV filename (default master_answer_key.csv): ").strip()
                filename = filename if filename else "master_answer_key.csv"
                assignment_key = input("Assignment key (Enter to use current): ").strip()
                assignment_key = assignment_key if assignment_key else None
                self.generate_master_student_answer_key(input_file, max_ex, filename, assignment_key)
        
            elif choice == '7':
                if not loaded_groups:
                    print("❌ No student groups loaded! Use option 3 to load groups first.")
                else:
                    assignment_key = input("Enter assignment key: ").strip()
                    if not assignment_key:
                        assignment_key = self.assignment_key or "DEFAULT"
                        print(f"Using assignment key: '{assignment_key}'")
                
                    max_ex = input("Maximum exercises (default 20): ").strip()
                    max_ex = int(max_ex) if max_ex else 20
                
                    self.generate_answer_keys_from_loaded_groups(loaded_groups, max_ex, assignment_key)
        
            elif choice == '8':
                student_id = input("Enter student ID/email: ").strip()
                if student_id:
                    group = self.get_student_group_letter(student_id)
                    group_num = self.get_student_group(student_id)
                    current_key = self.assignment_key or "DEFAULT"
                    print(f"Student '{student_id}' is assigned to: {group} (Group {group_num})")
                    print(f"Using assignment key: '{current_key}'")
                    
                    # Show sample codes
                    print("Sample progress codes for this student:")
                    for checkpoint in [5, 10, 15, 20]:
                        code = self.generate_progress_code(group_num, checkpoint, current_key)
                        print(f"  After {checkpoint} exercises: {code}")
        
            elif choice == '9':
                self.create_sample_student_file()
        
            elif choice == '10':
                print("Goodbye!")
                break
        
            else:
                print("Invalid choice. Please enter 1-10.")
    
    def create_sample_student_file(self):
        """Create a sample student file for testing"""
        sample_students = [
            "john.doe@university.edu",
            "jane.smith@university.edu", 
            "alice.johnson@university.edu",
            "bob.wilson@university.edu",
            "carol.brown@university.edu",
            "david.jones@university.edu",
            "emma.davis@university.edu",
            "frank.miller@university.edu",
            "grace.garcia@university.edu",
            "henry.rodriguez@university.edu"
        ]
        
        filename = "sample_students.txt"
        with open(filename, 'w') as f:
            for student in sample_students:
                f.write(student + '\n')
        
        print(f"📁 Sample student file created: {filename}")
        print("You can use this file to test the group assignment functionality.")

def main():
    """Main entry point"""
    generator = GroupHashGenerator()
    
    print("Group Hash Generator for Linux Tutorial")
    print("=" * 40)
    print("This utility helps you:")
    print("• Assign students to groups A-E based on their email/ID")
    print("• Generate progress code answer keys")
    print("• Export data for LMS integration")
    print()
    
    # Start interactive mode
    generator.interactive_mode()

if __name__ == "__main__":
    main()