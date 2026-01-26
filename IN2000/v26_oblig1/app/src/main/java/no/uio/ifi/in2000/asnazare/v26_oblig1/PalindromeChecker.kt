package no.uio.ifi.in2000.asnazare.v26_oblig1

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Create
import androidx.compose.material3.Button
import androidx.compose.material3.IconButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.focus.FocusRequester
import androidx.compose.ui.focus.focusRequester
import androidx.compose.ui.platform.LocalSoftwareKeyboardController
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun PalindromeChecker() {
    Column (
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ){
        Text (
            text = "Palindrome Checker",
            fontSize = 32.sp,
        )
        Spacer (modifier = Modifier.height(10.dp))

        var word by rememberSaveable { mutableStateOf("") }
        var result by rememberSaveable { mutableStateOf("") }
        val focusRequester = remember { FocusRequester() }
        var isClicked by rememberSaveable { mutableStateOf(false) }
        val keyboardController = LocalSoftwareKeyboardController.current // control for the keyboard

        OutlinedTextField(
            value = word,
            onValueChange = { word = it},
            label = { Text ( text = "type word")},
            leadingIcon = {
                IconButton(onClick = {}) {
                    Icon(
                        imageVector = Icons.Filled.Create,
                        contentDescription = "word"
                    )
                }
            },
            keyboardOptions = KeyboardOptions(
                imeAction = ImeAction.Done,
                keyboardType = KeyboardType.Email
            ),
            keyboardActions = KeyboardActions(
                onDone = {
                    isClicked = true
                    result = if (isPalindrome(word)) "'$word' is a palindrome" else "'$word' is NOT a palindrome"
                }
            ),
            //modifier = Modifier.focusRequester(focus)
        )
        Spacer (modifier = Modifier.height(10.dp))

        Button(
            modifier = Modifier
                .clickable { isClicked = !isClicked }
                .padding(20.dp),
            onClick = {
                isClicked = true
                keyboardController?.hide()
                result = if (isPalindrome(word)) "'$word' is a palindrome" else "'$word' is NOT a palindrome"
            }
        ) {
            Text("Check",
                modifier = Modifier.width((100.dp)),
                textAlign = TextAlign.Center
            )
        }
        if (isClicked){
            Text(result)
        }
    }
}

@Composable
@Preview(showBackground = true)
fun PalindromePreview(){
    PalindromeChecker()
}
