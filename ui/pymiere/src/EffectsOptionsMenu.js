import React from "react";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";
import ZoomEffect from "./Effects/ZoomEffect";
import PixelViewer from "./Effects/PixelViewer";
import TextOverlayMenu from './TextOverlayMenu'
import LightingOptionsMenu from "./LightingOptionsMenu";
import VignetteEffectPage from "./VignetteEffectPage";
import SpecialEffectsOptions from "./SpecialEffectsOptions";
import ColorMenu from "./ColorMenu";
import PencilTool from "./Effects/PencilTool";
import TransformationEditingMenu from "./TransformationEditingMenu.js";
import SizeEditingMenu from "./SizeEditingMenu.js";
import StoreLocalFilesystem from "./StoreLocalFilesystem";
import UploadNSTFilterForm from "./UploadNSTFilterForm";

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
        <Tab label="Text Overlay" {...a11yProps(0)} />
        <Tab label="Zoom" {...a11yProps(1)} />
        <Tab label="Pixel Viewer" {...a11yProps(2)} />
        <Tab label="Color Menu" {...a11yProps(3)} />
        <Tab label="Lighting Options" {...a11yProps(4)} />
        <Tab label="Special Effects" {...a11yProps(5)} />
        <Tab label="Pen Tool" {...a11yProps(6)} />
        <Tab label="Vignette" {...a11yProps(7)} />
        <Tab label="Transformation Menu" {...a11yProps(8)} />
        <Tab label="Size Editing Menu" {...a11yProps(9)} />
        <Tab label="Save As" {...a11yProps(10)} />
        <Tab label="NST Filters" {...a11yProps(11)} /> 
      </Tabs>
      <TabPanel value={value} index={0}>
        <TextOverlayMenu applyfilter={props.applyFilter}/>
      </TabPanel>
      <TabPanel value={value} index={1}>
          <ZoomEffect getCanvas={props.getCanvas} setCanvas={props.setCanvas} />
      </TabPanel>
      {/* TODO: pixel viewer text does not change from on to off when toggled*/}
      <TabPanel value={value} index={2}>
          <PixelViewer
            getCanvas={props.getCanvas}
            setCanvas={props.setCanvas}
          />
      </TabPanel>
      <TabPanel value={value} index={3}>
        <ColorMenu applyfilter={props.applyFilter}/>
      </TabPanel>
      <TabPanel value={value} index={4}>
        <LightingOptionsMenu />
      </TabPanel>
      <TabPanel value={value} index={5}>
        <SpecialEffectsOptions />
      </TabPanel>
      <TabPanel value={value} index={6}>
        <PencilTool getCanvas={props.getCanvas} setCanvas={props.setCanvas} />
      </TabPanel>
      <TabPanel value={value} index={7}>
        <VignetteEffectPage
          getCanvas={props.getCanvas}
          setCanvas={props.setCanvas}
        />
      </TabPanel>
      <TabPanel value={value} index={8}>
        <TransformationEditingMenu></TransformationEditingMenu>
      </TabPanel>
      <TabPanel value={value} index={9}>
        <SizeEditingMenu
          getCanvas={props.getCanvas}
          setCanvas={props.setCanvas}
        ></SizeEditingMenu>
      </TabPanel>
      <TabPanel value={value} index={10}>
        <StoreLocalFilesystem/>
      </TabPanel>
      <TabPanel value={value} index={11}>
        <UploadNSTFilterForm/>
      </TabPanel>
    </div>
  );
}
