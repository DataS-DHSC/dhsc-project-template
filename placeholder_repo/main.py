def main():
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
    from placeholder_module.run_pipeline import run_pipeline

    run_pipeline()
  
if __name__ == '__main__':
  main()