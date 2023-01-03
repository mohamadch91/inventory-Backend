SELECT  U.[ID]
      ,U.[name]
      ,U.[username]
      ,U.[password]
      ,U.[facilityID]
      ,U.[createby]
      ,U.[enable]
      ,U.[lastLogin]
      ,U.[creatondate]
      ,U.[idnumber]
      ,U.[position]
      ,U.[phone]
      ,U.[facadmin]
      ,U.[itemadmin]
      ,U.[reportadmin]
      ,U.[useradmin]
      ,F.[name] as facilityName
  FROM [inventory_jordan].[dbo].[user] as  U JOIN [inventory_jordan].[dbo].[facility] as  F
  ON U.facilityID=F.ID
