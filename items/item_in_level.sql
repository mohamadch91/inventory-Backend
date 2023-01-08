SELECT L.[ID]
      ,L.[itemTypeID]
      ,L.[level],
      I.name
  FROM [inventory_tls].[dbo].[itemTypeLevel] as L JOIN [inventory_tls].[dbo].[itemType] as I
  ON L.itemTypeID=I.ID