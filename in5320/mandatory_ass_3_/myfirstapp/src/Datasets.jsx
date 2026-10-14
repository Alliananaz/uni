import React, { useState } from 'react'
import { useDataQuery } from '@dhis2/app-runtime'
import { Menu, MenuItem, Table, TableHead, TableRowHead, TableCellHead, TableBody, TableRow, TableCell,} from "@dhis2/ui";
import styles from './Datasets.module.css'

const request = {
  request0: {
    resource: "dataSets",
    params: {
      fields: "id,displayName,created",
      paging: "false"
    }
  }
}


export function Datasets() {
    const { loading, error, data } = useDataQuery(request)
    const [selectedDataSet, setSelectedDataSet] = useState(null)

    if (error) {
        return <span>ERROR: {error.message}</span>
    }

    if (loading) {
        return <span>Loading...</span>
    }

    if (data) {
        console.log("API response:",data)
       //To-do: return a component using the data response 
        return (
            <div style= {{display: 'flex', alignItems: 'flex-start'}}>
                <Menu>
                    {data.request0.dataSets.map((dataSet) => (
                        <MenuItem key={dataSet.id} label={dataSet.displayName} active={selectedDataSet?.id === dataSet.id} onClick={() => setSelectedDataSet(dataSet)}/>
                    ))}
                </Menu>
                {selectedDataSet && (
                    <div className={styles.details}>
                        <Table>
                            <TableHead>
                                <TableRowHead>
                                    <TableCellHead>Display name</TableCellHead>
                                    <TableCellHead>ID</TableCellHead>
                                    <TableCellHead>Created</TableCellHead>
                                </TableRowHead>
                            </TableHead>
                            <TableBody>
                                <TableRow>
                                    <TableCell>{selectedDataSet.displayName}</TableCell>
                                    <TableCell>{selectedDataSet.id}</TableCell>
                                    <TableCell>{selectedDataSet.created}</TableCell>
                                </TableRow>
                            </TableBody>
                        </Table>
                    </div>
                )}
            </div>
        )
    }
}