# Python Number Guessing Game 🎯

> A simple, interactive number guessing game built with Python to practice fundamental programming concepts.

## 📝 Description

A command-line **Number Guessing Game** where the computer randomly selects a number between **1 and 10**, and the player has **only 3 tries** to guess it! Perfect for beginners learning Python logic and game flow.

## ✨ Features

- 🎲 Random number generation between 1 and 10
- ⏱️ Limited to 3 attempts for challenging gameplay
- 💡 Smart hints: **"Too High"** or **"Too Low"** after each guess
- 🔁 Replay option to play multiple rounds
- ✅ Input validation to handle errors gracefully
- 🏆 Win/lose feedback with encouraging messages

## 🚀 How to Play

1. **Run the game**
   ```bash
   python Number_Guessing.py
   ```

2. **Enter your guess** when prompted (number between 1-10)

3. **Follow the hints**:
   - If your guess is too high, you'll see "Too High!"
   - If your guess is too low, you'll see "Too Low!"
   - You have 3 chances to find the correct number

4. **Win or lose**:
   - Guess correctly within 3 tries = You Win! 🎉
   - Run out of tries = Game Over (correct number revealed)

5. **Play again?** Choose to replay or exit

## 🛠️ Installation

**Prerequisites**: Python 3.x

1. **Clone the repository**
   ```bash
   git clone https://github.com/tirth6851/Python-Number-guessing-Game.git
   cd Python-Number-guessing-Game
   ```

2. **Run the game**
   ```bash
   python Number_Guessing.py
   ```

No additional dependencies required!

## 📊 Game Flow

```
1. Computer picks random number (1-10)
   ↓
2. Player makes a guess
   ↓
3. Hint provided (Too High/Too Low)
   ↓
4. Repeat steps 2-3 (max 3 times)
   ↓
5. Result: Win or Lose
   ↓
6. Replay option
```

## 💻 Code Highlights

- **Random Module**: Uses `random.randint()` for number generation
- **While Loops**: Manages game rounds and replay functionality
- **Conditionals**: Implements game logic with if/elif/else
- **Input Validation**: Handles invalid inputs gracefully
- **Clean Code**: Well-commented and beginner-friendly

## 📚 Learning Objectives

This project demonstrates:
- Basic Python syntax and structure
- Control flow (loops, conditionals)
- User input handling
- Random number generation
- Game logic implementation
- Error handling fundamentals

## 📦 Project Structure

```
Python-Number-guessing-Game/
├── Number_Guessing.py  # Main game file
├── tests/              # Unit tests
├── LICENSE             # MIT License
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## 🧪 Testing

Basic tests are included in the `tests/` directory to verify game logic.

```bash
python -m pytest tests/
```

## 👨‍💻 About the Developer

Created by **Tirth Patel**, a Computer Science student at Cleveland State University learning Python programming and game development fundamentals.

- [GitHub Profile](https://github.com/tirth6851)
- [LinkedIn](https://www.linkedin.com/in/tirth-patel-949197346/)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🚀 Future Enhancements

Potential improvements:
- [ ] Difficulty levels (Easy: 5 tries, Hard: 2 tries)
- [ ] Wider number range option (1-100)
- [ ] Score tracking across multiple games
- [ ] Leaderboard system
- [ ] GUI version using Tkinter
- [ ] Multiplayer mode

## 💬 Feedback

Feedback and suggestions are welcome! Feel free to open an issue or submit a pull request.

---

**Last updated**: December 2025

*Made with ❤️ by Tirth Patel*
