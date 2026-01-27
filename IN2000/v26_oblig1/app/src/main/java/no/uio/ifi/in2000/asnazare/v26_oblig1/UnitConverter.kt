package no.uio.ifi.in2000.asnazare.v26_oblig1

import androidx.compose.foundation.ExperimentalFoundationApi
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.text2.input.rememberTextFieldState
import androidx.compose.foundation.text2.input.setTextAndPlaceCursorAtEnd
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ExposedDropdownMenuBox
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.MenuDefaults
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalSoftwareKeyboardController
import kotlinx.coroutines.selects.select

@OptIn(ExperimentalFoundationApi::class, ExperimentalMaterial3Api::class)
@Composable
fun UnitConverter(){
    Column(
        modifier = Modifier.fillMaxSize()
    ) {
        var number by rememberSaveable { mutableStateOf("") }
        var result by rememberSaveable { mutableStateOf("") }
        val keyboardController = LocalSoftwareKeyboardController.current // controller for the keyboard

        var isExpanded by rememberSaveable { mutableStateOf(false) }
        var units by rememberSaveable { mutableStateOf(ConverterUnits.entries) }
        var isClicked by rememberSaveable { mutableStateOf(false) }
        val textFieldState = rememberTextFieldState(ConverterUnits.entries.toString())
        var checkedIndex: Int? by remember {mutableStateOf(null)}

        ExposedDropdownMenuBox(
            expanded = isExpanded,
            onExpandedChange = { isExpanded = !isExpanded}
        ) {
            OutlinedTextField(
                readOnly = true,
                value = units.toString(),
                onValueChange = {},
                label = {
                        Text("Choose Unit")
                    }
            )
            ExposedDropdownMenu(
                expanded = isExpanded,
                onDismissRequest = { isExpanded = false }
            ) {
                ConverterUnits.entries.forEachIndexed { index, unit ->
                    DropdownMenuItem(
                        text = { Text( unit.toString(), style = MaterialTheme.typography.bodyLarge ) },
                        onClick = {
                            textFieldState.setTextAndPlaceCursorAtEnd(unit)
                            checkedIndex = index
                        },
                    )
                }
            }
        }
    }
}
