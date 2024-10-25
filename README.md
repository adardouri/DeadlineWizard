# DeadlineWizard

Effortlessly track and manage your deadlines with this lightweight CLI tool. Great for maintaining focus on tight schedules!

> **Note**: This project is currently under active development. The following TODO list tracks planned features and their implementation status.

## Current Development Status

### 1. Basic Structure and Core Functions
- [ ] Implement basic program structure (CLI command processing) - *needs refinement*
- [ ] Implement timer countdown and output (standard terminal display)
- [ ] Create file for storing deadlines (including date and priority) - *currently only supports time*

### 2. Implementation of Modes and Commands
- [ ] Implement set mode for entering new deadlines
  - [x] `-t` argument for time input
  - [ ] `-d` argument for day input
  - [ ] `-f` argument for full date and time
- [x] Implement delete mode for targeted deadline removal
- [x] Implement clear mode:
  - [x] `clear all` for complete removal
  - [x] `clear <ID>` for removing individual deadlines
  - [x] `clear past` for removing expired deadlines
- [ ] Implement live mode for dynamic timer display

### 3. Additional Functions and Features
- [ ] Priority levels for deadlines
- [ ] Reminder notifications at regular intervals
- [ ] Summary command for upcoming deadlines
- [ ] History function for completed deadlines
- [ ] History logging functionality

### 4. Supporting Features
- [x] Implementation of `-h` (help) - *continuous improvement ongoing*
- [ ] Flexible time input formats:
  - [x] HH:MM format (supports HHMM and 12-hour format with AM/PM)
  - [ ] INT for day input
  - [ ] YYYY-MM-DD HH:MM for full date
- [ ] Confirmation prompts for critical operations

### 5. Testing and Documentation
- [ ] Implementation tests for each mode and function
- [ ] Console output and user experience verification
- [ ] Complete GitHub documentation
  - [ ] Installation guide
  - [ ] Usage instructions
  - [ ] Examples