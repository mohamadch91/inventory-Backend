SELECT X.[ID]
      ,X.[itemTypeID]
      ,X.[fieldID]
      ,X.[req],
      F.fildName,
      T.name
  FROM [inventory_tls].[dbo].[itemField] as X JOIN [inventory_tls].[dbo].[field] as F
ON  X.fieldID=F.ID JOIN [inventory_tls].[dbo].[itemType] as T
    ON X.itemTypeID=T.ID