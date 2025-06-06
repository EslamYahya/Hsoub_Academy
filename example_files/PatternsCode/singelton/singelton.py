class DBConnection:
   __instance = None

   @staticmethod 
   def getInstance():
      if DBConnection.__instance == None:
         DBConnection()
         print("new instance has created")
      else:
         print("existed instance has returned")

      return DBConnection.__instance


   def query(self):
      # building query code here
        pass


if __name__ == "__main__":
   dbConnection = DBConnection.getInstance()
   print("writing query1 available now")
   dbConnection2 = DBConnection.getInstance()
   print("writing query2 available now")



