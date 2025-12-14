from normalize import normalize_phone_number



def main():
    print("Phone Normalizer")
    print("Paste a phone number and press Enter (Ctrl+C to exit)\n")

    while True:
        try:
            user_input = input("> ").strip()

            if not user_input:
                continue

            result = normalize_phone_number(user_input)

            if result.get("valid"):
                print("✔ Valid number")
                print(f"  E.164: {result['e164']}")
                print(f"  Plan: {result['plan']}")

                location = result.get("location")
                if isinstance(location, dict):
                    city = location.get("city", "Unknown")
                    region = location.get("region", "")
                    country = location.get("country", "")
                    print(f"  Location: {city}, {region} ({country})")
                else:
                    print("  Location: Unknown area code")

                if "warning" in result:
                    print(f"  ⚠ {result['warning']}")
            else:
                print("✖ Invalid number")
                print(f"  Reason: {result.get('reason')}")

            print()

        except KeyboardInterrupt:
            print("\nGoodbye.")
            break


if __name__ == "__main__":
    main()
