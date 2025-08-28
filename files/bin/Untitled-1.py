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
    
    def generate_progress_code(self, group_number: int, exercise_count: int) -> str:
        """Generate a 5-character progress code for a specific group"""
        # Create a seed based on group number and exercise count
        seed_string = f"GROUP{group_number}-{exercise_count}"
        
        # Convert string to numeric seed
        seed_value = hash(seed_string) % (2**32)
        
        # Seed the random number generator
        random.seed(seed_value)
        
        # Generate 5-character alphanumeric code
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        progress_code = ''.join(random.choices(characters, k=5))
        
        return progress_code
    
    def generate_answer_key_csv(self, max_exercises: int = 20, filename: str = "answer_key.csv") -> None:
        """Generate CSV file with answer keys for all groups"""
        checkpoints = list(range(self.progress_checkpoint, max_exercises + 1, self.progress_checkpoint))
        if max_exercises not in checkpoints:
            checkpoints.append(max_exercises)
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Header row
            header = ['Group'] + [f'Checkpoint_{cp}' for cp in checkpoints]
            writer.writerow(header)
            
            # Data rows
            for i, group_name in enumerate(self.group_names, 1):
                row = [group_name]
                for checkpoint in checkpoints:
                    code = self.generate_progress_code(i, checkpoint)
                    row.append(code)
                writer.writerow(row)
        
        print(f"📁 Answer key CSV generated: {filename}")
    
    def interactive_mode(self):
        """Interactive mode for testing and generating codes"""
        print("🖥️  INTERACTIVE GROUP HASH GENERATOR")
        print("=" * 50)
        
        while True:
            print("\nChoose an option:")
            print("1. Generate student groups from file")
            print("2. Generate answer key CSV")
            print("3. Test single student ID")
            print("4. Create sample student file")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                input_file = input("Student list filename (e.g., students.txt): ").strip()
                output_file = input("Output CSV filename (default: student_groups.csv): ").strip()
                output_file = output_file if output_file else "student_groups.csv"
                self.generate_student_groups_csv(input_file, output_file)
            
            elif choice == '2':
                max_ex = input("Maximum exercises (default 20): ").strip()
                max_ex = int(max_ex) if max_ex else 20
                filename = input("CSV filename (default answer_key.csv): ").strip()
                filename = filename if filename else "answer_key.csv"
                self.generate_answer_key_csv(max_ex, filename)
            
            elif choice == '3':
                student_id = input("Enter student ID/email: ").strip()
                if student_id:
                    group = self.get_student_group_letter(student_id)
                    print(f"Student '{student_id}' is assigned to: {group}")
            
            elif choice == '4':
                self.create_sample_student_file()
            
            elif choice == '5':
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter 1-5.")
    
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