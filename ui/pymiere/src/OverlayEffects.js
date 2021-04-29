import React from "react";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";
import TextOverlayMenu from "./TextOverlayMenu";
import PencilTool from "./Effects/PencilTool";
import MemeMaker from "./MemeMaker"
import EmojiOverlay from "./Effects/EmojiOverlay";

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
export default function OverlayEffects(props) {
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
        <Tab label="Pen Tool" {...a11yProps(1)} />
        <Tab label="Meme Maker" {...a11yProps(2)} />
        <Tab label="Emoji Overlay" {...a11yProps(3)} />
      </Tabs>

      <TabPanel value={value} index={0}>
        <TextOverlayMenu applyFilter={props.applyFilter} />
      </TabPanel>
      
      <TabPanel value={value} index={1}>
        <PencilTool applyFilter={props.applyFilter} getCanvas={props.getCanvas} setCanvas={props.setCanvas} />
      </TabPanel>
     
      <TabPanel value={value} index={2}>
        <MemeMaker applyFilter={props.applyFilter}/>
      </TabPanel>

      <TabPanel value={value} index={3}>
        <EmojiOverlay applyFilter={props.applyFilter} getCanvas={props.getCanvas} setCanvas={props.setCanvas}/>
      </TabPanel>

    </div>
  );
}
