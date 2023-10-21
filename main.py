import task.Workspace as Workspace
import task.Cli as Cli

Workspace(Cli().parse_args())
