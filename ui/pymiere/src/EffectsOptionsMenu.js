import React from "react";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";
import OverlayEffects from "./OverlayEffects"
import ColorAndLightingEffects from "./ColorAndLightingEffects"
import ViewingEffects from "./ViewingEffects";
import UploadImageToEdit from "./UploadImageToEdit"
import NSTEffects from "./NSTEffects";
import FileMenu from "./FileMenu";

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
    "aria-controls": `vertical-tabpanel-${index}`,
  };
}

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
    display: "flex",
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
        <Tab label="File" {...a11yProps(0)} />
        <Tab label="Overlays" {...a11yProps(1)} />
        <Tab label="Color and Lighting" {...a11yProps(2)} />
        <Tab label="Viewing" {...a11yProps(3)} />
        <Tab label="NST" {...a11yProps(4)} />
      </Tabs>
      <TabPanel value={value} index={0}>
        <FileMenu insertImage={props.insertImage} downloadImage={props.downloadImage}/>
      </TabPanel>
      <TabPanel value={value} index={1}>
        <OverlayEffects applyFilter={props.applyFilter} getCanvas={props.getCanvas} setCanvas={props.setCanvas} />
      </TabPanel>
      <TabPanel value={value} index={2}>
        <ColorAndLightingEffects applyFilter={props.applyFilter} getCanvas={props.getCanvas} setCanvas={props.setCanvas} />
      </TabPanel>
      <TabPanel value={value} index={3}>
        <ViewingEffects imageResolution={props.imageResolution} applyFilter={props.applyFilter} getCanvas={props.getCanvas} setCanvas={props.setCanvas} />
      </TabPanel>
      <TabPanel value={value} index={4}>
        <NSTEffects applyFilter={props.applyFilter} />
      </TabPanel>
      
    </div>
  );
}
