# Key-Logger

@startuml
package "Key Logger" {
    [Input Capture Module]
    [Storage Module]
    [Control Module]
    [Error Handling Module]
}

[Input Capture Module] --> [Storage Module] : Captured Data
[Control Module] --> [Input Capture Module] : Start/Stop Command
[Control Module] --> [Storage Module] : Configurations
[Error Handling Module] --> [Storage Module] : Error Logs

@endumlst