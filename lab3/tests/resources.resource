*** Settings ***
Documentation     This is a resource file, that can contain variables and keywords.
Library           TestLib.py
Library           Process

*** Variables ***
${cli}        /home/matt/kpi/qa-kp02-hatsenko/lab3/main.py
${cli-cmd}    python3

${dir}    directory
${bin}    binary-file
${log}    log-file
${buf}    buffer-file

${create}    create
${delete}    delete
${read}      read
${write}     write
${move}      move

${node-opt}         --node-type
${max-elems-opt}    --max-elems
${path-opt}         --path

${not-found}    error: Not Found

${success}    command was processed successfully

*** Keywords ***
Create directory
    [Arguments]    ${node_name}    ${max_elems}    ${path}
    
    ${opt1} =    Form Option    ${max-elems-opt}    ${max_elems}
    ${opt2} =    Form Option    ${path-opt}     ${path}
    ${result} =    Run Process    ${cli-cmd}    ${cli}    ${create}    ${dir}    ${node_name}    ${opt1}    ${opt2}
    
    Return From Keyword     ${result} 

Create Binary File
    [Arguments]    ${node_name}    ${path}    ${content}

    ${opt1} =    Form Option    ${path-opt}     ${path}
    ${result} =    Run Process    ${cli-cmd}    ${cli}    ${create}    ${bin}    ${content}    ${node_name}    ${opt1}
    
    Return From Keyword     ${result} 

Create Buffer File
    [Arguments]    ${node_name}    ${max_elems}    ${path}
    
    ${opt1} =    Form Option    ${max-elems-opt}    ${max_elems}
    ${opt2} =    Form Option    ${path-opt}     ${path}
    ${result} =    Run Process    ${cli-cmd}    ${cli}    ${create}    ${buf}    ${node_name}    ${opt1}    ${opt2}
    
    Return From Keyword     ${result} 

Create Log File
    [Arguments]    ${node_name}    ${path}
    ${opt1} =    Form Option    ${path-opt}     ${path}
    ${result} =    Run Process    ${cli-cmd}    ${cli}    ${create}    ${log}   ${node_name}    ${opt1}

    Return From Keyword    ${result} 

Read node
    [Arguments]    ${path}    ${node}

    ${opt1} =    Form Option    ${node-opt}    ${node}
    ${result} =    Run Process    ${cli-cmd}    ${cli}    ${read}    ${path}    ${opt1}
    
    Return From Keyword     ${result}

Delete node
    [Arguments]    ${path}

    ${result} =    Run Process    ${cli-cmd}    ${cli}    ${delete}    ${path}

    Return From Keyword     ${result}

Move node
    [Arguments]    ${path-to}    ${path-from}

    ${result} =    Run Process    ${cli-cmd}    ${cli}    ${move}    ${path-to}    ${path-from}

    Return From Keyword     ${result}

Write to node
    [Arguments]    ${path-to}    ${node}    ${content}

    ${opt1} =    Form Option    ${node-opt}    ${node}
    ${result} =    Run Process    ${cli-cmd}    ${cli}    ${write}    ${opt1}    ${path-to}    ${content}

    Return From Keyword     ${result}

Stop server
    ${result} =     Stop Docker
    Should Be Equal As Integers    ${result}    0