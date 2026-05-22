def caesar_encrypt(text, shift):
    """Encrypt text using Caesar Cipher with the given shift value."""
    result = []
    shift = shift % 26  # Normalize shift to 0-25
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(encrypted_char)
        else:
            result.append(char)
    
    return ''.join(result)


def caesar_decrypt(text, shift):
    """Decrypt text using Caesar Cipher with the given shift value."""
    return caesar_encrypt(text, -shift)


def display_banner():
    banner = """
╔══════════════════════════════════════════════════════════╗
║          🔐  CAESAR CIPHER TOOL  🔐                      ║
║          SkillCraft Technology - Task 01                 ║
╚══════════════════════════════════════════════════════════╝
    """
    print(banner)


def display_menu():
    print("\n" + "="*50)
    print("         MAIN MENU")
    print("="*50)
    print("  [1] Encrypt a message")
    print("  [2] Decrypt a message")
    print("  [3] Brute-force decrypt (try all shifts)")
    print("  [4] Exit")
    print("="*50)


def get_shift():
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("⚠  Please enter a value between 1 and 25.")
        except ValueError:
            print("⚠  Invalid input. Please enter a number.")


def brute_force_decrypt(text):
    print("\n" + "-"*50)
    print("  BRUTE-FORCE DECRYPTION (All 25 Shifts)")
    print("-"*50)
    for shift in range(1, 26):
        decrypted = caesar_decrypt(text, shift)
        print(f"  Shift {shift:2d}: {decrypted}")
    print("-"*50)


def main():
    display_banner()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            print("\n--- ENCRYPTION MODE ---")
            message = input("Enter the message to encrypt: ")
            shift = get_shift()
            encrypted = caesar_encrypt(message, shift)
            print(f"\n✅ Original Message : {message}")
            print(f"   Shift Value      : {shift}")
            print(f"   Encrypted Text   : {encrypted}")
        
        elif choice == '2':
            print("\n--- DECRYPTION MODE ---")
            message = input("Enter the message to decrypt: ")
            shift = get_shift()
            decrypted = caesar_decrypt(message, shift)
            print(f"\n✅ Encrypted Message : {message}")
            print(f"   Shift Value       : {shift}")
            print(f"   Decrypted Text    : {decrypted}")
        
        elif choice == '3':
            print("\n--- BRUTE-FORCE MODE ---")
            message = input("Enter the message to brute-force decrypt: ")
            brute_force_decrypt(message)
        
        elif choice == '4':
            print("\n👋 Thank you for using Caesar Cipher Tool!")
            print("   SkillCraft Technology - Task 01\n")
            break
        
        else:
            print("\n⚠  Invalid choice. Please enter 1, 2, 3, or 4.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
