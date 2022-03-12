if __name__ == "__main__":
   try:
       __import__("fcpro").vaumain()
   except Exception as e:
       exit(str(e))
