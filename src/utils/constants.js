import TimelineIcon from '@mui/icons-material/Timeline';
import BackupTableIcon from '@mui/icons-material/BackupTable';
import DashboardIcon from '@mui/icons-material/Dashboard';
import CodeIcon from '@mui/icons-material/Code';
import SecurityIcon from '@mui/icons-material/Security';
import NewReleasesIcon from '@mui/icons-material/NewReleases';
import TripOriginSharpIcon from '@mui/icons-material/TripOriginSharp';
import LayersSharpIcon from '@mui/icons-material/LayersSharp';
import AppShortcutSharpIcon from '@mui/icons-material/AppShortcutSharp';
import SettingsSharpIcon from '@mui/icons-material/SettingsSharp';


export const logo = 'https://i.ibb.co/s9Qys2j/logo.png';

export const categories = [
  { name: 'Timeline', icon: <TimelineIcon />, },
  { name: 'Backlog', icon: <BackupTableIcon /> },
  { name: 'Board', icon: <DashboardIcon />, },
  { name: 'Code', icon: <CodeIcon />, },
  { name: 'Security', icon: <SecurityIcon />, },
  { name: 'Releases', icon: <NewReleasesIcon />, },
  { name: 'Deployments', icon: <TripOriginSharpIcon />, },
  { name: 'Project Pages', icon: <LayersSharpIcon />, },
  { name: 'Slack Integration', icon: <CodeIcon />, },
  { name: 'Add Shortcut', icon: <AppShortcutSharpIcon />, },
  { name: 'Project Settings', icon: <SettingsSharpIcon />, },
];

export const stages = [
  { name: 'BACKLOG'},
  { name: 'ONGOING'},
  { name: 'READY FOR DEV'},
  { name: 'DEV IN PROGRESS'},
  { name: 'DESIGN REVIEW'},
  { name: 'CODE REVIEW'},
  { name: 'READY FOR QA'},
];