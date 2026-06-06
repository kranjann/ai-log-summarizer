from pathlib import Path

from llm import analyze_logs


BASE_DIR = Path(__file__).resolve().parent.parent

log_file = BASE_DIR / "logs" / "application_crash.log"


def main():
    try:
        with open(log_file, "r", encoding="utf-8") as file:
            logs = file.read()

        print("\n========== INPUT LOG ==========\n")
        print(logs)

        print("\n========== ANALYSIS ==========\n")

        analysis = analyze_logs(logs)

        print("\nSummary:")
        print(analysis.summary)

        print("\nRoot Cause:")
        print(analysis.root_cause)

        print("\nSeverity:")
        print(analysis.severity)

        print("\nRecommendations:")
        for recommendation in analysis.recommendations:
            print(f"- {recommendation}")

    except FileNotFoundError:
        print(f"Log file not found: {log_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()