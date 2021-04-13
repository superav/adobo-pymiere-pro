import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import TextOverlayTextInputFont from './TextOverlayTextInputFont'
import TextOverlayLocationSelector from './TextOverlayLocationSelector';

import Button from '@material-ui/core/Button'
import ZoomEffect from './Effects/ZoomEffect'
import PixelViewer from './Effects/PixelViewer'
import ColorMenu from './ColorMenu'

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`vertical-tabpanel-${index}`}
      aria-labelledby={`vertical-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box p={3}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `vertical-tab-${index}`,
    'aria-controls': `vertical-tabpanel-${index}`,
  };
}

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
    display: 'flex',
    height: 900,
  },
  tabs: {
    borderRight: `1px solid ${theme.palette.divider}`,
  },
}));

// TODO Add callbacks to TabPanel child elements to save their states between tab switches
export default function VerticalTabs(props) {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className={classes.root}>
      <Tabs
        orientation="vertical"
        value={value}
        onChange={handleChange}
        aria-label="Vertical tabs example"
        className={classes.tabs}
      >
        <Tab label="Text Overlay" {...a11yProps(0)} />
        <Tab label="Zoom" {...a11yProps(1)} />
        <Tab label="Pixel Viewer" {...a11yProps(2)} />
        <Tab label="Cropping" {...a11yProps(3)} />
        <Tab label="Color Menu" {...a11yProps(3)} />
        <Tab label="Item Five" {...a11yProps(4)} />
        <Tab label="Item Six" {...a11yProps(5)} />
        <Tab label="Item Seven" {...a11yProps(6)} />
      </Tabs>
      <TabPanel value={value} index={0}>
        <ul>
            <TextOverlayTextInputFont textLabel="Enter Text Below"/>
            <TextOverlayLocationSelector />
            <Button variant="contained" color="primary">Add Text Overlay</Button>

        </ul>
      </TabPanel>
      <TabPanel value={value} index={1}>
        <ul>
          <ZoomEffect getCanvas={props.getCanvas} setCanvas={props.setCanvas}/>
        </ul>
      </TabPanel>
      <TabPanel value={value} index={2}>
        <ul>
          <PixelViewer getCanvas={props.getCanvas} setCanvas={props.setCanvas}/>
        </ul>
      </TabPanel>
      <TabPanel value={value} index={3}>
        <ul>
          <CropEffect getCanvas={props.getCanvas} setCanvas={props.setCanvas}/>
          <ColorMenu />
        </ul>
      </TabPanel>
      <TabPanel value={value} index={4}>
        Item Five
      </TabPanel>
      <TabPanel value={value} index={5}>
        Item Six
      </TabPanel>
      <TabPanel value={value} index={6}>
        Item Seven
      </TabPanel>
    </div>
  );
}